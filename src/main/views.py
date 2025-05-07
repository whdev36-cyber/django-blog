from django.shortcuts import render
from .models import Post, Category, Widget
import random

# Home page view
def home(request):
    featured_post = Post.objects.filter(is_public=True, is_featured=True).order_by('-created_at').first()
    posts = Post.objects.filter(is_public=True).exclude(id=featured_post.id if featured_post else None)
    categories = Category.objects.all()
    widgets = Widget.objects.filter(is_active=True)
    widget = random.choice(widgets) if widgets.exists() else None
    return render(request, 'home.html', {
        'featured_post': featured_post,
        'posts': posts,
        'categories': categories,
        'widget': widget
    })


# About page view
def about(request):
    return render(request, 'about.html') # Render the about.html template

# YAY!
def yay(request):
    return render(request, 'yay.html') # Render the yay.html template