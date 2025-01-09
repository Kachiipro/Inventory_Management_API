from django.shortcuts import render
from rest_framework import status, permissions, filters
from rest_framework.response import Response
from items.models import Item, Category,InventoryLogs,Supplier
from .serializers import ItemSerializer, CategorySerializer, InventoryLogsSerializer,UserSerializer,InventoryLevelSerializer,SupplierSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import action
from .permissions import Isowner


# Create your views here.

User = get_user_model()

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class  = CategorySerializer
    permission_classes = [IsAuthenticated]
    
class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class  = SupplierSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def  destroy(self,request,*args, **kwargs):
        if self.get_object() == request.user:
            return super().destroy(request,*args,**kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    basename = 'Item'
    permission_classes =  [IsAuthenticated, Isowner]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields =['category', 'price']
    ordering_fields =['name','price','category','quantity']
    
    def p_create(self, serializer):
        serializer.save(created_by=self.request.User)
    


   
    
    
    @action(methods=['post'], detail=True)  # restock
    def restock(self, request, pk=None):
        item = self.get_object()
        quantity = request.data.get('quantity')
        if quantity:
            item.quantity += quantity
            item.save()
            InventoryLogs.objects.create(
                item=item,
                user=request.user,
                action='Restock',
                quantity =request.data['quantity']
            )
            serializer = self.get_serializer(item)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=True)  #sold stock
    def sold_stock(self, request, pk=None):
        item = self.get_object()
        quantity = request.data.get('quantity')
        if quantity:
            item.quantity -= quantity
            item.save()
            InventoryLogs.objects.create(
                item=item,
                user=request.user,
                action='subtract',
                quantity =request.data['quantity']
            )
            serializer = self.get_serializer(item)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
class ActionViewSet(ReadOnlyModelViewSet):
    queryset = InventoryLogs.objects.all()
    serializer_class= InventoryLogsSerializer
    permission_classes =  [IsAuthenticated]



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    
class InventoryLevelview(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = InventoryLevelSerializer
    basename = 'Inventory-item'
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.BaseFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields =['category', 'price']
    ordering_fields =['name','price','category','quantity']
    filterset_fields = ['quantity']
    
    def filter_queryset(self, queryset):
            low_stock = self.request.query_params.get('low_stock')

            if low_stock:
                threshold = 50  # the threshold value 
                queryset = queryset.filter(quantity__lte=threshold)

            return queryset

