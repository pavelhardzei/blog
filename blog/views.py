from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all(), 'title': 'Home'})


@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})