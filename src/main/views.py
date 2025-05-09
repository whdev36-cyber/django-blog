from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Widget
import random
from django.http import HttpResponse

def home(request):
    featured_post = Post.objects.filter(is_public=True, is_featured=True).order_by('-created_at').first()
    posts = Post.objects.filter(is_public=True).exclude(id=featured_post.id if featured_post else None).order_by('-created_at')

    # Paginator
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'home.html', {
        'featured_post': featured_post,
        'page_obj': page_obj,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return HttpResponse(category.name)


def search(request):
    return HttpResponse('search')

# About page view
def about(request):
    return render(request, 'about.html') # Render the about.html template

# YAY!
def yay(request):
    return render(request, 'yay.html') # Render the yay.html template