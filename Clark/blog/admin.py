from django.contrib import admin
from .models import Home, About, Resume, Service, Skill, Project, Categorie, Tag, Blog
from comment.models import Comment
# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_update', 'created_at']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'phone', 'last_update', 'created_at']


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_update', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    filter_horizontal = ['tag']
    inlines = [CommentInLine]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'created_at']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    search_fields = ['text']
    list_filter = ['text']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Resume)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Categorie, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
