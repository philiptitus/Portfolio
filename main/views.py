from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from django.http import JsonResponse


from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Certificate,
		Skill,
		Project,
		Video,
		WebhookEvent
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True).order_by('-date')
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)

		context["skills"] = skills
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context





class ContactView(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/success/"

    def form_valid(self, form):
        form.save()

        # Email to the contact form submitter
        subject_submitter = 'Thank you for reaching out'
        message_submitter = f"Dear {form.cleaned_data['name']},\n\n Hey Thank you for reaching out to me. I have received your message and will get back to you soon.\n\nBest regards,\nPhilip Titus"
        send_mail(subject_submitter, message_submitter, settings.EMAIL_HOST_USER, [form.cleaned_data['email']])

        # Email to mrphilipowade@gmail.com
        subject_admin = 'New Contact Form Submission'
        message_admin = f"Hello,\n\nYou have a new contact form submission on your website:\n\nName: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}\n\n"
        send_mail(subject_admin, message_admin, settings.EMAIL_HOST_USER, ['mrphilipowade@gmail.com'])

        return super().form_valid(form)



class PrivacyView(generic.TemplateView):
    template_name = "main/privacy.html"


class NotFoundView(generic.TemplateView):
    template_name = "main/404.html"


class Success(generic.TemplateView):

	template_name = "main/success.html"


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)


		videos = Video.objects.all

		context["videos"] = videos


		return context

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"



	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)


		videos = Video.objects.all

		context["videos"] = videos


		return context

class ProjectView(generic.ListView):
	model = Project
	template_name = "main/project.html"

	def get_queryset(self):
		return super().get_queryset().all()

class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = "main/project-detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)


		videos = Video.objects.all

		context["videos"] = videos


		return context


class DSView(generic.ListView):
	model = Blog
	template_name = "main/categories/dscience.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		skills = Skill.objects.all
		videos = Video.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["skills"] = skills
		context["videos"] = videos
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()





class WebDevelopment(generic.ListView):
	model = Blog
	template_name = "main/categories/web.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		videos = Video.objects.all

		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)


		context["videos"] = videos

		context["projects"] = projects
		context["skills"] = skills
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()

class MobileDevelopment(generic.ListView):
	model = Blog
	template_name = "main/categories/mobile.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		videos = Video.objects.all
		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["skills"] = skills
		context["videos"] = videos
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()





class CyberSecurity(generic.ListView):
	model = Blog
	template_name = "main/categories/cyber.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		videos = Video.objects.all
		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["skills"] = skills
		context["videos"] = videos
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()







class CloudComputing(generic.ListView):
	model = Blog
	template_name = "main/categories/cloud.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		videos = Video.objects.all
		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["skills"] = skills
		context["videos"] = videos
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()




class Game(generic.ListView):
	model = Blog
	template_name = "main/categories/game.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		videos = Video.objects.all
		skills = Skill.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["videos"] = videos
		context["skills"] = skills
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()



class Other(generic.ListView):
	model = Blog
	template_name = "main/categories/other.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = Project.objects.all()
		skills = Skill.objects.all
		videos = Video.objects.all
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)



		context["projects"] = projects
		context["videos"] = videos
		context["skills"] = skills
		context["certificates"] = certificates
		context["portfolio"] = portfolio

		return context

	def get_queryset(self):
		return super().get_queryset().all()


class Development(generic.TemplateView):
	template_name = 'main/six.html'




class LatestEventsView(ListView):
    model = WebhookEvent
    queryset = WebhookEvent.objects.order_by('-timestamp')[:10]
    context_object_name = 'events'

    def render_to_response(self, context, **response_kwargs):
        # Extract only the specified fields for each event
        events = list(context['events'].values('commit_url', 'repository_url', 'repository', 'description', 'timestamp'))
        return JsonResponse(events, safe=False)