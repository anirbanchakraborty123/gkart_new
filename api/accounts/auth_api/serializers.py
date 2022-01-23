from unicodedata import numeric
from rest_framework import serializers
from ..models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    

    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()

    
    class Meta:
        
        model=  Account
        fields=['id','username','email','is_active','is_admin','is_superuser']
        #fields='__all__'


    #Validator for the serializer-- to validate the api post parameters
    def validate(self,data):
        #query=Account.objects.all()
        print(data)
        user = self.context.get("request").method
        print(user)
        if user=='POST':
                if data['is_admin'] is False:
                    raise serializers.ValidationError({'error':'is_admin should be true'})
                    return data

        return data