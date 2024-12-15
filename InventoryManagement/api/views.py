from django.shortcuts import render
from items.models import Item, Category,ActionLogs
from users.models import Role
from .serializers import ItemSerializer, CategorySerializer, ActionlogsSerializer, RoleSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
# Create your views here.

User = get_user_model()

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class  = CategorySerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    
class ActionViewSet(ReadOnlyModelViewSet):
    queryset = ActionLogs.objects.all()
    serializer_class= ActionlogsSerializer
    permission_classes = [IsAuthenticated]

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
    

