from django.core.management.base import BaseCommand
from main.models import MLModel
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all MLModel objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        mlmodels = MLModel.objects.all()
        for mlmodel in mlmodels:
            updated = False
            # Embed name
            if mlmodel.name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=mlmodel.name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    mlmodel.name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed name for {mlmodel}: {e}"))
            # Embed body
            if mlmodel.body:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=mlmodel.body,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    mlmodel.body_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed body for {mlmodel}: {e}"))
            if updated:
                mlmodel.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded MLModel: {mlmodel}")) 