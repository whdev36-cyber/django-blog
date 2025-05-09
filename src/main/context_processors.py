from .models import Category, Widget
import random

def blog_context(request):
    categories = Category.objects.all()
    widgets = Widget.objects.filter(is_active=True)
    widget = random.choice(widgets) if widgets.exists() else None
    return {
        'categories': categories,
        'widget': widget
    }
