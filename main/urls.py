from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
    path('success/', views.Success.as_view(), name="success"),
    path('privacy/', views.PrivacyView.as_view(), name="privacy"),
    path('404/', views.NotFoundView.as_view(), name="404"),
    path('api/blogs/', views.BlogListJsonView.as_view(), name='blog-list-json'),

    path('new/', views.LatestEventsView.as_view(), name='latest_events'),
    path('ml-models/', views.MLModelListView.as_view(), name="mlmodels"),
    path('development/', views.Development.as_view(), name="dev"),
	path('contact/', views.ContactView.as_view(), name="contact"),
    path('project/', views.ProjectView.as_view(), name="projects"),
	path('datascience/', views.DSView.as_view(), name="dscience"),
    path('webdevelopment/', views.WebDevelopment.as_view(), name="webdevelopment"),
    path('mobiledevelopment/', views.MobileDevelopment.as_view(), name="mobiledevelopment"),
    path('cybersecurity/', views.CyberSecurity.as_view(), name="cybersecurity"),
    path('cloudcomputing/', views.CloudComputing.as_view(), name="cloud"),
    path('games/', views.Game.as_view(), name="game"),
    path('other/', views.Other.as_view(), name="other"),
	path('project/<slug:slug>', views.ProjectDetailView.as_view(), name="project"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
    path('ml-model/<slug:slug>/', views.MLModelDetailView.as_view(), name="mlmodel_detail"),

	]