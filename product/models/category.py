from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "category"
            slug = base_slug
            suffix = 1
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                suffix += 1
                slug = f"{base_slug}-{suffix}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self
