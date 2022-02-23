from django.urls import path
from . import views

urlpatterns=[
        path('register/' ,views.Register, name='register'),
        path('login/' ,views.Login, name='login'),
        path('logout/' ,views.Logout, name='logout'),
        # path('add_to_cart/<int:product_id>/' ,views.add_to_cart, name='add_to_cart'),

]