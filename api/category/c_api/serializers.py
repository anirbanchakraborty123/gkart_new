from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    

    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()

    cart_image = serializers.ImageField(max_length=None,
            allow_empty_file=False,allow_null=True,required=False)
            
    class Meta:
        
        model=  Category
        
        #fields = ['id','category_name','description','status']
        fields= '__all__'