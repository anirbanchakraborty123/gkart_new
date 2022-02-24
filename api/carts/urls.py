from django.urls import path
from . import views

urlpatterns=[
        path('' ,views.cart_products, name='cart'),
        path('add_to_cart/<int:product_id>/' ,views.add_to_cart, name='add_to_cart'),

]