from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    stock_status = models.CharField(max_length=50)
    available_stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.sku})"
