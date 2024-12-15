from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100, unique= True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='items',)
    quantity = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='items')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name

    
class ActionLogs(models.Model):
    action = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.action} by {self.user} on {self.item}"