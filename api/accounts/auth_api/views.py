
from rest_framework import viewsets
from .serializers import AccountSerializer
from ..models  import Account
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,BasePermission

# Code for Custom Permissions
class WriteOnlyByAdmin(BasePermission):
    
    def has_permission(self, request, view):
        user= request.user

        if request.method=='GET':
            return True

        # if request.method=='POST':
           
        #     if user.is_superuser:
        #         return True

        if request.method=='PUT':
           
            if user.is_superuser:
                return True

        if request.method=='PATCH':
           
            if user.is_superuser:
                return True

        if request.method=='DELETE':
           
            if user.is_superuser:
                return True
        return False


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
 
    queryset=Account.objects.all()
    serializer_class= AccountSerializer
    permission_classes =[WriteOnlyByAdmin]
    
