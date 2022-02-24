from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.SimpleRouter()
router.register(r'cart', views.CartViewSet )
router.register(r'cartitems', views.CartItemsViewSet )
urlpatterns = [
    path('', include(router.urls ))
]