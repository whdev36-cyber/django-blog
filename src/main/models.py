from django.db import models
from django.utils.text import slugify

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
    

class Post(models.Model): pass