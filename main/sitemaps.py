from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Portfolio, Blog, Project, MLModel

class StaticSitemap(Sitemap):
    def items(self):
        return [
            'main:home',
            'main:success',
            'main:privacy',
            'main:404',
            'main:latest_events',
            'main:mlmodels',
            'main:dev',
            'main:contact',
            'main:projects',
            'main:dscience',
            'main:webdevelopment',
            'main:mobiledevelopment',
            'main:cybersecurity',
            'main:cloud',
            'main:game',
            'main:other',
            'main:portfolios',
            'main:blogs'
        ]
    
    def location(self, item):
        return reverse(item)


class PortfolioSitemap(Sitemap):
    def items(self):
        return Portfolio.objects.filter(is_active=True)
    
    def location(self, obj):
        return obj.get_absolute_url()


class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.filter(is_active=True)[:100]
    
    def location(self, obj):
        return obj.get_absolute_url()


class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()[:100]
    
    def location(self, obj):
        return obj.get_absolute_url()


class MLModelSitemap(Sitemap):
    def items(self):
        return MLModel.objects.filter(is_active=True)[:100]
    
    def location(self, obj):
        return obj.get_absolute_url() 