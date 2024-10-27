from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import GithubWebhookView


urlpatterns = [
    path('philip/', admin.site.urls),
    path('', include('main.urls', namespace="main")),
    path('webhook/github/', GithubWebhookView.as_view(), name='github-webhook'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
