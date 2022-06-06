from django.shortcuts import render
from django.utils import timezone
from .models import Post

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/main.html', {'posts': posts})

def aboutMe(request):
    return render(request, 'blog/aboutMe.html', {})

def Portfolio(request):
    return render(request, 'blog/Portfolio.html', {})

def Contact(request):
    return render(request, 'blog/Contact.html', {})