from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Peter Wright',
        'title': 'Blog Post 1',
        'content': 'Post 1 content',
        'date_posted': '5/6/2019'
    },
    {
        'author': 'Paul Smith',
        'title': 'Blog Post 2',
        'content': 'Post 2 content',
        'date_posted': '5/6/2019'
    }
]


def home(request):

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



