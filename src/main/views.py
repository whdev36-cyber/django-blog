from django.shortcuts import render
from .models import Post, Category

# Home page view
def home(request):
    posts = Post.objects.filter(is_public=True).all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})

# About page view
def about(request):
    return render(request, 'about.html') # Render the about.html template

# YAY!
def yay(request):
    return render(request, 'yay.html') # Render the yay.html template