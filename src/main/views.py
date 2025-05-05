from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html') # Render the home.html template

# About page view
def about(request):
    return render(request, 'about.html') # Render the about.html template

# YAY!
def yay(request):
    return render(request, 'yay.html') # Render the yay.html template