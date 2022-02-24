from rest_framework import viewsets
from .serializers import CartSerializer,CartItemsSerializer
from ..models import Cart,CartItems
from ..views import _cart_id

# Create your views here.

class CartViewSet(viewsets.ModelViewSet):

    queryset=Cart.objects.all().order_by('id')
    serializer_class=CartSerializer

class CartItemsViewSet(viewsets.ModelViewSet):

    queryset=CartItems.objects.all().order_by('id')
    serializer_class=CartItemsSerializer