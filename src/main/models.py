from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    '''
    Tag model to represent a tag in the system.
    '''
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model): pass
class Post(models.Model): pass