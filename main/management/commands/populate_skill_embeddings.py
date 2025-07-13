from django.core.management.base import BaseCommand
from main.models import Skill
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate name_embedding for all Skill objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        skills = Skill.objects.all()
        for skill in skills:
            if not skill.name:
                continue
            try:
                response = genai.embed_content(
                    model="models/embedding-001",
                    content=skill.name,
                    task_type="RETRIEVAL_DOCUMENT"
                )
                embedding = response["embedding"]
                skill.name_embedding = json.dumps(embedding)
                skill.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded skill: {skill.name}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed for {skill.name}: {e}")) 