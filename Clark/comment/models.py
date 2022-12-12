from django.db import models
from blog.models import Blog
# Create your models here.

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()


    def __str__(self):
        return self.name