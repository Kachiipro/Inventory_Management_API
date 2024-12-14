from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class Item(models.Model):
    name = models.CharField(max_length=100, unique= True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='items')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True) 