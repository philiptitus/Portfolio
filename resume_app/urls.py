from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import GithubWebhookView
# from main.chatbot_views import chatbot_api


urlpatterns = [
    path('philip/', admin.site.urls),
    path('', include('main.urls', namespace="main")),
    path('webhook/github/', GithubWebhookView.as_view(), name='github-webhook'),
    # path('api/chatbot/', chatbot_api, name='chatbot-api'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
