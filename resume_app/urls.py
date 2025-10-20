from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from .views import GithubWebhookView
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticSitemap, PortfolioSitemap, BlogSitemap, ProjectSitemap, MLModelSitemap
# from main.chatbot_views import chatbot_api

sitemaps = {
    'static': StaticSitemap,
    'portfolios': PortfolioSitemap,
    'blogs': BlogSitemap,
    'projects': ProjectSitemap,
    'mlmodels': MLModelSitemap,
}

urlpatterns = [
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('philip/', admin.site.urls),
    path('', include('main.urls', namespace="main")),
    path('webhook/github/', GithubWebhookView.as_view(), name='github-webhook'),
    # path('api/chatbot/', chatbot_api, name='chatbot-api'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
