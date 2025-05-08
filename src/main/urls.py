from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Home page
    path('about/', views.about, name='about'), # About page
    path('yay/', views.yay, name='yay'), # YAY!
    path('post/detail/<int:id>/', views.post_detail, name='post_detail'), # Post detail page
    path('category/detail/<slug:slug>/', views.category_detail, name='category_detail'), # Category detail page
    path('search/', views.search, name='search'), # Search
]