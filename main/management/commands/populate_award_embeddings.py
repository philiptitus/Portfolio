from django.core.management.base import BaseCommand
from main.models import Award
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all Award objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        awards = Award.objects.all()
        for award in awards:
            updated = False
            # Embed title
            if award.title:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=award.title,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    award.title_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed title for {award}: {e}"))
            # Embed description
            if award.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=award.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    award.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {award}: {e}"))
            if updated:
                award.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded Award: {award}")) 