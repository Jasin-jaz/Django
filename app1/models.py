from django.db import models

# Create your models here.

# Profile
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name  

# Colors of products
class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

# Product
class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    color = models.ManyToManyField(Color)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
