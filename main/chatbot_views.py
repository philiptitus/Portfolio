from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from main.models import Portfolio, UserProfile, Skill, MLModel, Project, Blog, Certificate, Award, JobExperience
import google.generativeai as genai
import numpy as np
import json
import os

# Configure Gemini
api_key = os.environ.get('GEMINI_API_KEY')
if api_key:
    genai.configure(api_key=api_key)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

@csrf_exempt
@require_http_methods(["POST"])
def chatbot_api(request):
    """Chatbot API endpoint that searches through portfolio data."""
    try:
        # Parse JSON request
        data = json.loads(request.body)
        question = data.get('question', '').strip()
        
        if not question:
            return JsonResponse({
                'error': 'Question is required'
            }, status=400)
        
        if not api_key:
            return JsonResponse({
                'error': 'Gemini API key not configured'
            }, status=500)
        
        # Embed the user question
        question_response = genai.embed_content(
            model="models/embedding-001",
            content=question,
            task_type="RETRIEVAL_DOCUMENT"
        )
        question_embedding = question_response["embedding"]
        
        # Search through all model embeddings
        similarities = []
        
        # Search Portfolio embeddings
        portfolios = Portfolio.objects.all()
        for portfolio in portfolios:
            portfolio_similarities = []
            if portfolio.name_embedding:
                try:
                    name_emb = json.loads(portfolio.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    portfolio_similarities.append(('name', sim))
                except:
                    pass
            if portfolio.description_embedding:
                try:
                    desc_emb = json.loads(portfolio.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    portfolio_similarities.append(('description', sim))
                except:
                    pass
            if portfolio.body_embedding:
                try:
                    body_emb = json.loads(portfolio.body_embedding)
                    sim = cosine_similarity(question_embedding, body_emb)
                    portfolio_similarities.append(('body', sim))
                except:
                    pass
            if portfolio_similarities:
                max_sim = max(portfolio_similarities, key=lambda x: x[1])
                similarities.append(('portfolio', portfolio, max_sim[1]))
        
        # Search UserProfile embeddings
        profiles = UserProfile.objects.all()
        for profile in profiles:
            if profile.bio_embedding:
                try:
                    bio_emb = json.loads(profile.bio_embedding)
                    sim = cosine_similarity(question_embedding, bio_emb)
                    similarities.append(('userprofile', profile, sim))
                except:
                    pass
        
        # Search Skill embeddings
        skills = Skill.objects.all()
        for skill in skills:
            if skill.name_embedding:
                try:
                    name_emb = json.loads(skill.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    similarities.append(('skill', skill, sim))
                except:
                    pass
        
        # Search MLModel embeddings
        mlmodels = MLModel.objects.all()
        for mlmodel in mlmodels:
            mlmodel_similarities = []
            if mlmodel.name_embedding:
                try:
                    name_emb = json.loads(mlmodel.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    mlmodel_similarities.append(('name', sim))
                except Exception as e:
                    pass
            if mlmodel.body_embedding:
                try:
                    body_emb = json.loads(mlmodel.body_embedding)
                    sim = cosine_similarity(question_embedding, body_emb)
                    mlmodel_similarities.append(('body', sim))
                except Exception as e:
                    pass
            if mlmodel_similarities:
                max_sim = max(mlmodel_similarities, key=lambda x: x[1])
                similarities.append(('mlmodel', mlmodel, max_sim[1]))
        
        # Search Project embeddings
        projects = Project.objects.all()
        for project in projects:
            project_similarities = []
            if project.name_embedding:
                try:
                    name_emb = json.loads(project.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    project_similarities.append(('name', sim))
                except:
                    pass
            if project.description_embedding:
                try:
                    desc_emb = json.loads(project.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    project_similarities.append(('description', sim))
                except:
                    pass
            if project.body_embedding:
                try:
                    body_emb = json.loads(project.body_embedding)
                    sim = cosine_similarity(question_embedding, body_emb)
                    project_similarities.append(('body', sim))
                except:
                    pass
            if project_similarities:
                max_sim = max(project_similarities, key=lambda x: x[1])
                similarities.append(('project', project, max_sim[1]))
        
        # Search Blog embeddings
        blogs = Blog.objects.all()
        for blog in blogs:
            blog_similarities = []
            if blog.name_embedding:
                try:
                    name_emb = json.loads(blog.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    blog_similarities.append(('name', sim))
                except Exception as e:
                    pass
            if blog.description_embedding:
                try:
                    desc_emb = json.loads(blog.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    blog_similarities.append(('description', sim))
                except Exception as e:
                    pass
            if blog.body_embedding:
                try:
                    body_emb = json.loads(blog.body_embedding)
                    sim = cosine_similarity(question_embedding, body_emb)
                    blog_similarities.append(('body', sim))
                except Exception as e:
                    pass
            if blog_similarities:
                max_sim = max(blog_similarities, key=lambda x: x[1])
                similarities.append(('blog', blog, max_sim[1]))
        
        # Search Certificate embeddings
        certificates = Certificate.objects.all()
        for certificate in certificates:
            cert_similarities = []
            if certificate.name_embedding:
                try:
                    name_emb = json.loads(certificate.name_embedding)
                    sim = cosine_similarity(question_embedding, name_emb)
                    cert_similarities.append(('name', sim))
                except:
                    pass
            if certificate.title_embedding:
                try:
                    title_emb = json.loads(certificate.title_embedding)
                    sim = cosine_similarity(question_embedding, title_emb)
                    cert_similarities.append(('title', sim))
                except:
                    pass
            if certificate.description_embedding:
                try:
                    desc_emb = json.loads(certificate.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    cert_similarities.append(('description', sim))
                except:
                    pass
            if cert_similarities:
                max_sim = max(cert_similarities, key=lambda x: x[1])
                similarities.append(('certificate', certificate, max_sim[1]))
        
        # Search Award embeddings
        awards = Award.objects.all()
        for award in awards:
            award_similarities = []
            if award.title_embedding:
                try:
                    title_emb = json.loads(award.title_embedding)
                    sim = cosine_similarity(question_embedding, title_emb)
                    award_similarities.append(('title', sim))
                except:
                    pass
            if award.description_embedding:
                try:
                    desc_emb = json.loads(award.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    award_similarities.append(('description', sim))
                except:
                    pass
            if award_similarities:
                max_sim = max(award_similarities, key=lambda x: x[1])
                similarities.append(('award', award, max_sim[1]))
        
        # Search JobExperience embeddings
        jobs = JobExperience.objects.all()
        for job in jobs:
            job_similarities = []
            if job.job_title_embedding:
                try:
                    title_emb = json.loads(job.job_title_embedding)
                    sim = cosine_similarity(question_embedding, title_emb)
                    job_similarities.append(('job_title', sim))
                except:
                    pass
            if job.company_name_embedding:
                try:
                    company_emb = json.loads(job.company_name_embedding)
                    sim = cosine_similarity(question_embedding, company_emb)
                    job_similarities.append(('company_name', sim))
                except:
                    pass
            if job.location_embedding:
                try:
                    location_emb = json.loads(job.location_embedding)
                    sim = cosine_similarity(question_embedding, location_emb)
                    job_similarities.append(('location', sim))
                except:
                    pass
            if job.description_embedding:
                try:
                    desc_emb = json.loads(job.description_embedding)
                    sim = cosine_similarity(question_embedding, desc_emb)
                    job_similarities.append(('description', sim))
                except:
                    pass
            if job_similarities:
                max_sim = max(job_similarities, key=lambda x: x[1])
                similarities.append(('job', job, max_sim[1]))
        
        # Sort by similarity and get top 8 (increased to include more diverse results)
        similarities.sort(key=lambda x: x[2], reverse=True)
        top_items = similarities[:8]
        
        # Priority boosting for different content types
        ml_ai_keywords = ['machine learning', 'ml', 'ai', 'artificial intelligence', 'deep learning', 'neural network', 'model', 'algorithm', 'prediction', 'classification', 'regression', 'clustering', 'data science', 'tensorflow', 'pytorch', 'scikit', 'keras']
        blog_keywords = ['blog', 'article', 'post', 'writing', 'content', 'published']
        question_lower = question.lower()
        is_ml_ai_question = any(keyword in question_lower for keyword in ml_ai_keywords)
        is_blog_question = any(keyword in question_lower for keyword in blog_keywords)
        
        if is_ml_ai_question:
            # Boost ML model scores significantly
            boosted_similarities = []
            for item_type, item, similarity in similarities:
                if item_type == 'mlmodel':
                    # Boost ML model scores by 0.2 (making them much higher priority)
                    boosted_score = similarity + 0.2
                    boosted_similarities.append((item_type, item, boosted_score))
                else:
                    boosted_similarities.append((item_type, item, similarity))
            
            # Re-sort with boosted scores
            boosted_similarities.sort(key=lambda x: x[2], reverse=True)
            top_items = boosted_similarities[:8]
        elif is_blog_question:
            # Boost blog scores significantly
            boosted_similarities = []
            for item_type, item, similarity in similarities:
                if item_type == 'blog':
                    # Boost blog scores by 0.2 (making them much higher priority)
                    boosted_score = similarity + 0.2
                    boosted_similarities.append((item_type, item, boosted_score))
                else:
                    boosted_similarities.append((item_type, item, similarity))
            
            # Re-sort with boosted scores
            boosted_similarities.sort(key=lambda x: x[2], reverse=True)
            top_items = boosted_similarities[:8]
        else:
            # Smart filtering: If question is about projects/work, ensure we include some actual projects
            project_keywords = ['project', 'work', 'built', 'created', 'developed', 'application', 'app']
            is_project_question = any(keyword in question_lower for keyword in project_keywords)
            
            if is_project_question:
                # Check if we have projects in top 8, if not, add some
                project_types = ['portfolio', 'mlmodel', 'project', 'blog']
                has_projects = any(item[0] in project_types for item in top_items)
                
                if not has_projects:
                    # Find the best project and add it
                    project_items = [item for item in similarities if item[0] in project_types]
                    if project_items:
                        # Replace the lowest scoring item with the best project
                        best_project = project_items[0]
                        top_items = top_items[:-1] + [best_project]
                        top_items.sort(key=lambda x: x[2], reverse=True)
        

        
        if not top_items:
            return JsonResponse({
                'answer': 'I don\'t have enough information to answer that question about my background and work.',
                'relevant_items': []
            })
        
        # Build context from top items
        context = "Based on my background and work, here's what I can tell you:\n\n"
        for item_type, item, similarity in top_items:
            if item_type == 'portfolio':
                context += f"Portfolio Project: {item.name}\n"
                if item.description:
                    context += f"Description: {item.description}\n"
                if item.body:
                    import re
                    clean_body = re.sub('<[^<]+?>', '', item.body)
                    context += f"Details: {clean_body[:300]}...\n"
                context += f"Category: {item.category}\n"
                context += f"Core Skill: {item.core_skill}\n\n"
            elif item_type == 'userprofile':
                context += f"About Me: {item.bio}\n\n"
            elif item_type == 'skill':
                context += f"Skill: {item.name} (Score: {item.score})\n\n"
            elif item_type == 'mlmodel':
                context += f"ML Model: {item.name}\n"
                if item.body:
                    import re
                    clean_body = re.sub('<[^<]+?>', '', item.body)
                    context += f"Details: {clean_body[:300]}...\n"
                context += f"Category: {item.category}\n\n"
            elif item_type == 'project':
                context += f"Project: {item.name}\n"
                if item.description:
                    context += f"Description: {item.description}\n"
                if item.body:
                    import re
                    clean_body = re.sub('<[^<]+?>', '', item.body)
                    context += f"Details: {clean_body[:300]}...\n"
                context += f"Status: {item.status}\n"
                context += f"Category: {item.category}\n\n"
            elif item_type == 'blog':
                context += f"Blog Post: {item.name}\n"
                if item.description:
                    context += f"Description: {item.description}\n"
                if item.body:
                    import re
                    clean_body = re.sub('<[^<]+?>', '', item.body)
                    context += f"Content: {clean_body[:300]}...\n"
                context += f"Category: {item.category}\n\n"
            elif item_type == 'certificate':
                context += f"Certificate: {item.name}\n"
                if item.title:
                    context += f"Title: {item.title}\n"
                if item.description:
                    context += f"Description: {item.description}\n\n"
            elif item_type == 'award':
                context += f"Award: {item.title}\n"
                if item.description:
                    context += f"Description: {item.description}\n"
                context += f"Issued by: {item.issued_by}\n\n"
            elif item_type == 'job':
                context += f"Job: {item.job_title} at {item.company_name}\n"
                if item.location:
                    context += f"Location: {item.location}\n"
                if item.description:
                    context += f"Description: {item.description}\n"
                context += f"Period: {item.start_date} to {item.end_date if item.end_date else 'Present'}\n\n"
        
        # Generate answer using Gemini Pro
        model = genai.GenerativeModel("gemini-2.5-pro")
        prompt = f"""
        You are Philip, the owner of this portfolio website. A visitor asked: "{question}"
        
        Here is relevant information about me and my work:
        {context}
        
        Respond as Philip speaking directly to the visitor in first person. Use "I", "my", "me" - speak naturally and confidently as if you are Philip himself.
        
        For example:
        - Say "I have experience with..." not "Philip has experience with..."
        - Say "My skills include..." not "His skills include..."
        - Say "I worked on..." not "He worked on..."
        
        Provide a helpful and accurate answer based ONLY on the information provided above. 
        If the information doesn't contain enough details to answer the question, say so politely.
        Keep your response conversational, friendly, and authentically Philip.
        """
        
        response = model.generate_content(prompt)
        answer = response.text
        
        # Prepare relevant items for response
        relevant_items = []
        for item_type, item, similarity in top_items:
            if item_type == 'portfolio':
                relevant_items.append({
                    'type': 'portfolio',
                    'name': item.name,
                    'description': item.description,
                    'category': item.category,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'userprofile':
                relevant_items.append({
                    'type': 'userprofile',
                    'name': 'About Me',
                    'description': item.bio,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'skill':
                relevant_items.append({
                    'type': 'skill',
                    'name': item.name,
                    'description': f"Skill with score: {item.score}",
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'mlmodel':
                relevant_items.append({
                    'type': 'mlmodel',
                    'name': item.name,
                    'description': item.body[:200] + "..." if item.body else "",
                    'category': item.category,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'project':
                relevant_items.append({
                    'type': 'project',
                    'name': item.name,
                    'description': item.description,
                    'category': item.category,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'blog':
                relevant_items.append({
                    'type': 'blog',
                    'name': item.name,
                    'description': item.description,
                    'category': item.category,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'certificate':
                relevant_items.append({
                    'type': 'certificate',
                    'name': item.name,
                    'description': item.description,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'award':
                relevant_items.append({
                    'type': 'award',
                    'name': item.title,
                    'description': item.description,
                    'issued_by': item.issued_by,
                    'similarity_score': round(similarity, 3)
                })
            elif item_type == 'job':
                relevant_items.append({
                    'type': 'job',
                    'name': f"{item.job_title} at {item.company_name}",
                    'description': item.description,
                    'location': item.location,
                    'similarity_score': round(similarity, 3)
                })
        
        return JsonResponse({
            'answer': answer,
            'relevant_items': relevant_items
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': f'An error occurred: {str(e)}'
        }, status=500) 