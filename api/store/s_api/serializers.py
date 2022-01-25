from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()

    #cart_image = serializers.ImageField(max_length=None,
           # allow_empty_file=False,allow_null=True,required=False)
            

    #to show the category name instead of category url in json response
    category= serializers.ReadOnlyField(source='category.category_name')    


    class Meta:
        
        model=  Product
        
        #fields = ['id','category_name','description','status']
        fields= '__all__'