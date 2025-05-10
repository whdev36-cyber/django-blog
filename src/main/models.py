from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import markdown
import bleach

# Tag model
class Tag(models.Model):
    '''
    Tag model to represent a tag in the system.
    '''
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Category model
class Category(models.Model):
    '''
    Category model used to group related posts or items.
    Each category has a unique name and a slug for SEO-friendly URLs.
    '''

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    '''
    Post model represents a piece of content such as an article or blog post.
    It includes a title, author, content body, optional image or image URL,
    category, tags, source reference, and tracking fields like views and caps.
    Timestamps for creation and last update are also recorded.
    '''

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    # image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)
    source = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    caps = models.PositiveIntegerField(default=0)
    is_public = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def clean(self):
    #     if self.image and self.image_url:
    #         raise ValidationError('Only one of image or image_url should be set.')
        
    def __str__(self):
        return self.title
    
    @property
    def content_html(self):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        html = markdown.markdown(self.content, output_format='html', extensions=['fenced_code', 'codehilite'])
        cleaned = bleach.clean(html, tags=allowed_tags, strip=True)
        return bleach.linkify(cleaned)
    

# class Comment(models.Model): pass

class Widget(models.Model):
    '''
    Widget model represents a small application or component that can be embedded
    in a web page. It includes a title, content, and an optional image.
    '''

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='widgets/images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  