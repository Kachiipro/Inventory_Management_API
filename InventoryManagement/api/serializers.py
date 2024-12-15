from rest_framework import serializers
from items.models import Item, Category, ActionLogs
from users.models import Role
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = '__all__'
class ActionlogsSerializer(serializers.Serializer):
    class Meta:
        model = ActionLogs
        fields = '__all__'
class RoleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Role
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "role","password")
        
    def validate_password(self, value):


        return make_password(value)
