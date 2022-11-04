from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet,basename="customer")
router.register(r'orders', views.OrderViewSet,basename="order")
router.register(r'items', views.ItemViewSet,basename="item")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]