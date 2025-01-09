from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model() # custom user import

class Category(models.Model):  # category model
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
    
class Supplier(models.Model):  # supplier model
    name =models.CharField(max_length=200, null= False, blank=False, unique=True)
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):  # item model
    name = models.CharField(max_length=100, unique= True,null=False, blank= False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='items',)
    quantity = models.IntegerField(null=False , blank= False)
    price = models.DecimalField(null=False,max_digits =5,decimal_places = 2, blank=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='items', null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='items')
    date_added = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name

    
class InventoryLogs(models.Model):  #inventory logs model
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[
        ('restock', 'Restock'),
        ('subtract', 'Subtract')
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.item} - {self.action} {self.quantity} by {self.user.username}'
