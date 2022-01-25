from django.urls import path,include
#from rest_framework.authtoken import views
from rest_framework import routers
from. import views


router = routers.SimpleRouter()
router.register(r'', views.CategoryViewSet)
#urlpatterns=router.urls 
urlpatterns = [
    path('', include(router.urls))
]