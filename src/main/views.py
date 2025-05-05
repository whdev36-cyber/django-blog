from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html') # Render the home.html template
