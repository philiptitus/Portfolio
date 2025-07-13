from django.core.management.base import BaseCommand
from main.models import Project
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all Project objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        projects = Project.objects.all()
        for project in projects:
            updated = False
            # Embed name
            if project.name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=project.name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    project.name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed name for {project}: {e}"))
            # Embed description
            if project.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=project.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    project.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {project}: {e}"))
            # Embed body
            if project.body:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=project.body,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    project.body_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed body for {project}: {e}"))
            if updated:
                project.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded Project: {project}")) 