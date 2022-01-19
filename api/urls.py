from django.urls import path,include
from rest_framework.authtoken import views
from . import views
urlpatterns = [
    path('', views.home, name='api.home'),
    path('category/', include('api.category.c_api.urls')),
    path('product/', include('api.store.s_api.urls')),

]