from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Tom',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 23, 2021'
    },
    {
        'author': 'Bob',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 23, 2021'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context=context)