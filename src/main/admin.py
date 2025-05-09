from django.contrib import admin
from .models import Tag, Category, Post, Widget

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'views', 'caps', 'created_at']
    # search_fields = ['title', 'author__username', 'category__name']
    list_filter = ['author', 'category', 'tags', 'created_at']
    readonly_fields = ['views', 'caps', 'created_at', 'updated_at']
    # autocomplete_fields = ['author', 'category', 'tags']

class WidgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ['title', 'content']

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Widget, WidgetAdmin)
