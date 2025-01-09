from rest_framework import serializers
from items.models import Item, Category,InventoryLogs,Supplier
from django.contrib.auth import get_user_model



User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):  #category serializer
    class Meta:
        model = Category
        fields = '__all__'
        
class SupplierSerializer(serializers.ModelSerializer): #supplier seriarlizer
    class Meta:
        model =  Supplier
        fields = '__all__' 

class ItemSerializer(serializers.ModelSerializer): #Item serializer
    
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['created_by']
        
    def create(self, validated_data):   # validate and get user that creates item
        validated_data['created_by'] = self.context['request'].user
        return Item.objects.create(**validated_data)


class InventoryLogsSerializer(serializers.ModelSerializer): #logs  serializers
    class Meta:
        model = InventoryLogs
        fields = '__all__'
        

    
class UserSerializer(serializers.ModelSerializer): #user serializer
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

class InventoryLevelSerializer(serializers.ModelSerializer): #inventory serializer
    class Meta:
        model = Item
        fields = ['name','category','price','quantity']


