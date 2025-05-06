from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Category(models.Model): pass
class Post(models.Model): pass