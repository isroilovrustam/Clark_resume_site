from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=303)
    message = models.TextField()

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactMe(models.Model):
    image = models.ImageField(null=True, blank=True)
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=202)


    def __str__(self):
        return self.name