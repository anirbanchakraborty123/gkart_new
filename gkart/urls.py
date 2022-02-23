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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('api.accounts.urls'), name='accounts'),
    path('' , views.home, name='home'),
    path('search/' ,views.search_product, name='search_stores'),
    path('store/' ,include('api.store.urls'), name='store'),
    path('cart/' ,include('api.carts.urls'), name='cart'),
    path('api-auth/', include('rest_framework.urls')),  
    path('api/' ,include('api.urls'), name='api'),
    path('ajax_calls/search/', views.autocomplete, name='autocomplete'),
    path('ajax_calls/update_cart/', views.update_cart, name='update_cart'),
    path('ajax_calls/cart_deatils/', views.cart_details, name='cart_details'),
    

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns=[
#         path('__debug__/', include('debug_toolbar.urls')),
#     ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
