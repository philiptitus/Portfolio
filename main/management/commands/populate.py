from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import MLModel, Skill
from django.core.files.base import ContentFile
import random
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates the database with 10 sample ML models'

    def handle(self, *args, **kwargs):
        # First, create some sample skills if they don't exist
        ml_skills = [
            'TensorFlow',
            'PyTorch',
            'Scikit-learn',
            'Keras',
            'NumPy',
            'Pandas',
            'OpenCV',
            'NLTK',
            'SpaCy',
            'XGBoost'
        ]

        # Create skills
        skills = []
        for skill_name in ml_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={'is_key_skill': True}
            )
            skills.append(skill)

        # Sample ML model data
        sample_models = [
            {
                'name': 'Image Classification CNN',
                'category': 'COMPUTER_VISION',
                'body': 'A convolutional neural network model for image classification using PyTorch. Features transfer learning with ResNet50 architecture.',
                'tier': 'S',
            },
            {
                'name': 'Sentiment Analysis BERT',
                'category': 'NATURAL_LANGUAGE_PROCESSING',
                'body': 'Fine-tuned BERT model for sentiment analysis on product reviews, achieving 94% accuracy.',
                'tier': 'S',
            },
            {
                'name': 'Customer Segmentation',
                'category': 'CLUSTERING',
                'body': 'K-means clustering model for customer segmentation using purchasing behavior data.',
                'tier': 'A',
            },
            {
                'name': 'Stock Price Predictor',
                'category': 'TIME_SERIES',
                'body': 'LSTM-based deep learning model for stock price prediction using historical market data.',
                'tier': 'A',
            },
            {
                'name': 'Recommendation Engine',
                'category': 'RECOMMENDATION_SYSTEMS',
                'body': 'Collaborative filtering model for product recommendations using matrix factorization.',
                'tier': 'A',
            },
            {
                'name': 'Fraud Detection System',
                'category': 'ANOMALY_DETECTION',
                'body': 'Anomaly detection model using isolation forest for identifying fraudulent transactions.',
                'tier': 'B',
            },
            {
                'name': 'Object Detection YOLOv5',
                'category': 'COMPUTER_VISION',
                'body': 'Real-time object detection model using YOLOv5 architecture.',
                'tier': 'S',
            },
            {
                'name': 'Text Summarization',
                'category': 'NATURAL_LANGUAGE_PROCESSING',
                'body': 'Transformer-based model for automatic text summarization.',
                'tier': 'A',
            },
            {
                'name': 'Customer Churn Predictor',
                'category': 'SUPERVISED_LEARNING',
                'body': 'XGBoost model for predicting customer churn using historical customer data.',
                'tier': 'B',
            },
            {
                'name': 'Reinforcement Learning Game Bot',
                'category': 'REINFORCEMENT_LEARNING',
                'body': 'Deep Q-learning model trained to play classic Atari games.',
                'tier': 'S',
            },
        ]

        # Create ML models
        for model_data in sample_models:
            # Create the model
            ml_model = MLModel.objects.create(
                name=model_data['name'],
                body=model_data['body'],
                category=model_data['category'],
                tier=model_data['tier'],
                date=timezone.now(),
                github_url=f"https://github.com/yourusername/{slugify(model_data['name'])}",
                is_active=True,
            )

            # Add random skills (between 3 and 6) to each model
            num_skills = random.randint(3, 6)
            selected_skills = random.sample(skills, num_skills)
            ml_model.skills.add(*selected_skills)

            self.stdout.write(
                self.style.SUCCESS(f'Successfully created ML model: {ml_model.name}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample ML models')
        )
