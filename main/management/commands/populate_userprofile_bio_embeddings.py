from django.core.management.base import BaseCommand
from main.models import UserProfile
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate bio_embedding for all UserProfile objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        profiles = UserProfile.objects.all()
        for profile in profiles:
            if not profile.bio:
                continue
            try:
                response = genai.embed_content(
                    model="models/embedding-001",
                    content=profile.bio,
                    task_type="RETRIEVAL_DOCUMENT"
                )
                embedding = response["embedding"]
                profile.bio_embedding = json.dumps(embedding)
                profile.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded bio for: {profile}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed for {profile}: {e}")) 