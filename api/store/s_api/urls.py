from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.SimpleRouter()
router.register(r'', views.ProductViewSet )
urlpatterns = [
    path('', include(router.urls ))
]

# urlpatterns = [
#     path('', views.ProductViewSet.as_view, name="api_product")
# ]
