from django.core.management.base import BaseCommand
from main.models import Certificate
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all Certificate objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        certificates = Certificate.objects.all()
        for certificate in certificates:
            updated = False
            # Embed name
            if certificate.name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=certificate.name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    certificate.name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed name for {certificate}: {e}"))
            # Embed title
            if certificate.title:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=certificate.title,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    certificate.title_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed title for {certificate}: {e}"))
            # Embed description
            if certificate.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=certificate.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    certificate.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {certificate}: {e}"))
            if updated:
                certificate.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded Certificate: {certificate}")) 