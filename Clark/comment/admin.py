from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website']
    list_filter = ['blog']



admin.site.register(Comment, CommentAdmin)