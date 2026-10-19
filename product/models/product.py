from django.db import models
from product.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products",
        null=True, blank=True,
    )

    def __str__(self):
        return self.name

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self
