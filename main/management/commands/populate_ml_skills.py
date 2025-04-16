from django.core.management.base import BaseCommand
from main.models import Skill

class Command(BaseCommand):
    help = 'Populates the database with ML-related skills'

    def handle(self, *args, **kwargs):
        # Comprehensive list of ML skills organized by categories
        ml_skills = {
            # Core ML Libraries and Frameworks
            'Machine Learning Frameworks': [
                'TensorFlow',
                'PyTorch',
                'Keras',
                'Scikit-learn',
                'JAX',
                'MXNet',
                'Caffe',
                'FastAI',
                'LightGBM',
                'XGBoost',
                'CatBoost',
            ],
            
            # Deep Learning Specific
            'Deep Learning': [
                'Neural Networks',
                'CNN',
                'RNN',
                'LSTM',
                'GAN',
                'Transformers',
                'Transfer Learning',
                'AutoEncoders',
                'Reinforcement Learning',
            ],
            
            # NLP Tools and Libraries
            'Natural Language Processing': [
                'NLTK',
                'SpaCy',
                'Gensim',
                'Hugging Face',
                'Word2Vec',
                'BERT',
                'GPT',
                'T5',
                'RoBERTa',
                'Tokenization',
            ],
            
            # Computer Vision
            'Computer Vision': [
                'OpenCV',
                'PIL/Pillow',
                'YOLO',
                'ImageAI',
                'Detectron2',
                'MediaPipe',
                'TorchVision',
            ],
            
            # Data Processing and Analysis
            'Data Processing': [
                'NumPy',
                'Pandas',
                'Dask',
                'PySpark',
                'Scipy',
                'Matplotlib',
                'Seaborn',
                'Plotly',
                'Bokeh',
                'Databricks',
            ],
            
            # ML Ops and Deployment
            'ML Operations': [
                'Docker',
                'Kubernetes',
                'MLflow',
                'Kubeflow',
                'TensorBoard',
                'DVC',
                'Weights & Biases',
                'Ray',
                'Airflow',
                'Prefect',
            ],
            
            # Cloud ML Services
            'Cloud ML': [
                'AWS SageMaker',
                'Google Cloud AI',
                'Azure ML',
                'IBM Watson',
                'Vertex AI',
            ],
            
            # Specialized ML Areas
            'Specialized Skills': [
                'Time Series Analysis',
                'Anomaly Detection',
                'Recommendation Systems',
                'Feature Engineering',
                'Model Optimization',
                'Hyperparameter Tuning',
                'A/B Testing',
                'Model Interpretability',
                'Data Augmentation',
                'Ensemble Methods',
            ],
            
            # ML Development Tools
            'Development Tools': [
                'Jupyter Notebooks',
                'VS Code',
                'Git',
                'GitHub',
                'GitLab',
                'Anaconda',
                'Poetry',
                'PyCharm',
            ],
            
            # Database and Big Data
            'Data Management': [
                'SQL',
                'MongoDB',
                'Redis',
                'Hadoop',
                'Spark',
                'Hive',
                'Cassandra',
                'Neo4j',
            ]
        }

        # Counter for created skills
        created_count = 0
        updated_count = 0

        # Create or update skills
        for category, skills in ml_skills.items():
            for skill_name in skills:
                skill, created = Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        'is_key_skill': True,
                        'score': 80  # Default score
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'Created new skill: {skill_name}')
                    )
                else:
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'Skill already exists: {skill_name}')
                    )

        # Final summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully populated ML skills:\n'
                f'Created: {created_count}\n'
                f'Already existed: {updated_count}\n'
                f'Total skills: {created_count + updated_count}'
            )
        )
