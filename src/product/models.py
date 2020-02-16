from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, null=True, 
                on_delete=models.SET_NULL, related_name="products")
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
