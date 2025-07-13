from django.core.management.base import BaseCommand
from main.models import Portfolio
import google.generativeai as genai
import os
import json

class Command(BaseCommand):
    help = 'Populate embedding fields for all Portfolio objects using Gemini Pro embeddings.'

    def handle(self, *args, **options):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.stderr.write(self.style.ERROR('GEMINI_API_KEY environment variable not set.'))
            return
        genai.configure(api_key=api_key)

        portfolios = Portfolio.objects.all()
        for portfolio in portfolios:
            updated = False
            # Embed name
            if portfolio.name:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=portfolio.name,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    portfolio.name_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed name for {portfolio}: {e}"))
            # Embed description
            if portfolio.description:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=portfolio.description,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    portfolio.description_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed description for {portfolio}: {e}"))
            # Embed body
            if portfolio.body:
                try:
                    response = genai.embed_content(
                        model="models/embedding-001",
                        content=portfolio.body,
                        task_type="RETRIEVAL_DOCUMENT"
                    )
                    portfolio.body_embedding = json.dumps(response["embedding"])
                    updated = True
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed body for {portfolio}: {e}"))
            if updated:
                portfolio.save()
                self.stdout.write(self.style.SUCCESS(f"Embedded portfolio: {portfolio}")) 