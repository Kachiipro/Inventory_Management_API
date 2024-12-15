from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('Item',views.ItemViewSet)
router.register('Category',views.CategoryViewSet)
router.register('User', views.UserViewSet)
router.register('Role', views.RoleViewSet)
router.register('Actionlogs', views.ActionViewSet)



urlpatterns = [] + router.urls
