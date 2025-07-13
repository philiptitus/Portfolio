from django.core.management.base import BaseCommand
from main.models import JobExperience
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all JobExperience objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        jobs = JobExperience.objects.all()
        for job in jobs:
            updated = False
            # Embed job_title
            if job.job_title:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=job.job_title,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    job.job_title_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed job_title for {job}: {e}"))
            # Embed company_name
            if job.company_name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=job.company_name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    job.company_name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed company_name for {job}: {e}"))
            # Embed location
            if job.location:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=job.location,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    job.location_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed location for {job}: {e}"))
            # Embed description
            if job.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=job.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    job.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {job}: {e}"))
            if updated:
                job.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded JobExperience: {job}")) 