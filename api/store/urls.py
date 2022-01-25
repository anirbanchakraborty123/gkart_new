"""gkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views

urlpatterns = [
<<<<<<< HEAD:api/store/urls.py
    path('' , views.store, name='store'),
    path('<slug:category_slug>/' , views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/' , views.product_details, name='product_details'),
=======
    path('' , views.store, name='store_home'),
    path('<slug:category_slug>/' , views.store, name='products_by_category'),

>>>>>>> main:store/urls.py
]