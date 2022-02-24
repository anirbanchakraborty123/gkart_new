from rest_framework import serializers
from api.carts.models import Cart,CartItems
class CartSerializer(serializers.HyperlinkedModelSerializer):


    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()

    class Meta:
        model  = Cart
        fields = '__all__'
    
class CartItemsSerializer(serializers.HyperlinkedModelSerializer):


    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()
    
    class Meta:
        model  = CartItems
        fields = '__all__'