from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=202)
    occupation = models.CharField(max_length=202)
    image = models.ImageField()

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=202)
    text = models.CharField(max_length=202)
    name = models.CharField(max_length=202)
    birth = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    code = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    image = models.ImageField()
    project = models.IntegerField()


    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    start_finish = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    text = models.TextField()


    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.CharField(max_length=202)
    title = models.CharField(max_length=202)

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    prosent = models.IntegerField()

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=202)
    name = models.CharField(max_length=100)

    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag")
    image = models.ImageField()
    title = models.CharField(max_length=202)
    text = models.CharField(max_length=202)
    last_update = models.DateTimeField(auto_now=True)
    contentone = models.TextField()
    contenttwo = models.TextField()
    creative = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-id"]