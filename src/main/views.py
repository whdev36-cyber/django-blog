from django.shortcuts import render
from .models import Post, Category
import random

# Home page view
def home(request):
    featured_post = Post.objects.filter(is_public=True, is_featured=True).order_by('-created_at').first()
    posts = Post.objects.filter(is_public=True).exclude(id=featured_post.id if featured_post else None)
    categories = Category.objects.all()
    widget_messages = [
        "Discover more articles and tips tailored just for you.",
        "Stay updated with the latest trends in programming.",
        "Join our newsletter and never miss an update.",
        "Need inspiration? Check out our featured posts!",
        "Follow us for more developer stories and resources."
    ]
    widget_message = random.choice(widget_messages)
    return render(request, 'home.html', {
        'featured_post': featured_post,
        'posts': posts,
        'categories': categories,
        'widget_message': widget_message
    })


# About page view
def about(request):
    return render(request, 'about.html') # Render the about.html template

# YAY!
def yay(request):
    return render(request, 'yay.html') # Render the yay.html template