from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telegram_user_id = models.BigIntegerField(default=None, unique=True)
    current_page = models.IntegerField(default=0)

class Product_Group(models.Model):
    name = models.CharField(max_length=50)

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

class Product(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField()
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, blank=True, null=True)
    product_group = models.ForeignKey(Product_Group, on_delete=models.RESTRICT, blank=True, null=True)
