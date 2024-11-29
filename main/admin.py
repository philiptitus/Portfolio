from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill,
    Project,
    Video,
    WebhookEvent,
    Award,
    JobExperience
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'is_active')
#     readonly_fields = ('slug',)

#     # Make the skills field appear with a filter widget
#     filter_horizontal = ('skills',)  # This makes ManyToManyFields easier to manage

#     # Optionally, include the skills field in the fields or fieldsets
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'description', 'core_skill', 'category', 'skills', 'is_active', 'slug', 'body')
#         }),
#         ('Media', {
#             'fields': ('image', 'image_url' ,'imager', 'imager_url','app', 'url', 'url_2', 'url_3', 'amazon_url')
#         }),
#         ('Other', {
#             'fields': ('date', 'star', 'featured')
#         }),
#     )
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'core_skill', 'is_active']
    filter_horizontal = ('skills',)  # Enables the dual list selection widget for skills

admin.site.register(Portfolio, PortfolioAdmin)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('date','name','for_sale')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
        list_display = ('url','text',)

admin.site.register(WebhookEvent)
admin.site.register(Award)
admin.site.register(JobExperience)

