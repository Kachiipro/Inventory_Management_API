from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views 
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import MyTokenObtainPairView


router = DefaultRouter()
router.register('item',views.ItemViewSet, basename='')
router.register('category',views.CategoryViewSet)
router.register('Supplier',views.SupplierViewSet)
router.register('user', views.UserViewSet)
router.register('inventorylogs', views.ActionViewSet)
router.register('inventory', views.InventoryLevelview, basename='Inventory-item')



urlpatterns = [path('token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),] + router.urls
