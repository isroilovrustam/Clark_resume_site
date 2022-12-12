from django.shortcuts import render, redirect
from .models import Home, About, Resume, Service, Skill, Project, Blog, Categorie, Tag
from comment.models import Comment
from comment.forms import CommentForm
from contact.models import ContactMe
from contact.forms import ContactForm
# Create your views here.


def index(request):
    object_home = Home.objects.all()
    object_about = About.objects.all()
    object_resume = Resume.objects.all()
    object_service = Service.objects.all()
    object_skill = Skill.objects.all()
    object_project = Project.objects.all()
    object_blog = Blog.objects.all()
    object_contactme = ContactMe.objects.all()
    form = ContactForm(request.POST or None)
    url = request.META.get("HTTP_REFERER")
    if form.is_valid():
        form.save()
        return redirect(url)
    context = {
        'form': form,
        'contactmes': object_contactme,
        'homes':object_home,
        'abouts': object_about,
        'resumes': object_resume,
        'services': object_service,
        'skills': object_skill,
        'projects': object_project,
        'blogs': object_blog,
    }

    return render(request, 'base.html', context)



def single(request, pk):
    object_single = Blog.objects.get(id=pk)
    object_categorie = Categorie.objects.all()
    object_blog = Blog.objects.all()[:3]
    object_tag = Tag.objects.all()
    form = CommentForm(request.POST or None)
    url = request.META.get("HTTP_REFERER")
    if form.is_valid():
        var = form.save(commit=False)
        var.blog = object_single
        var.save()
        return redirect(url)
    context = {
        'form': form,
        'single': object_single,
        'categories': object_categorie,
        'blogs': object_blog,
        'tags': object_tag,
    }


    return render(request, 'single.html', context)