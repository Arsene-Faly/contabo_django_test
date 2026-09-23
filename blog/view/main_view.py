from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Article

def home_view(request):
    context = {
        'page' : 'home'
    }
    return render(request, 'pages/users/index.html', context)

def service_view(request):
    context = {
        'page' : 'service'
    }
    return render(request, 'pages/users/services.html', context)

def about_view(request):
    context = {
        'page' : 'about'
    }
    return render(request, 'pages/users/about.html', context)

@login_required
def blog_view(request):
    articles = Article.objects.all()
    
    context = {
        'page' : 'blog',
        'articles' : articles
    }
    return render(request, 'pages/users/blog.html', context)

def blog_detail_view(request):
    context = {
        'page' : 'home'
    }
    return render(request, 'pages/users/blog-detail.html', context)