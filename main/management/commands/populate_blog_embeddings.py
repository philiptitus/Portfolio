from django.core.management.base import BaseCommand
from main.models import Blog
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all Blog objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        blogs = Blog.objects.all()
        for blog in blogs:
            updated = False
            # Embed name
            if blog.name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=blog.name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    blog.name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed name for {blog}: {e}"))
            # Embed description
            if blog.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=blog.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    blog.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {blog}: {e}"))
            # Embed body
            if blog.body:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=blog.body,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    blog.body_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed body for {blog}: {e}"))
            if updated:
                blog.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded Blog: {blog}")) 