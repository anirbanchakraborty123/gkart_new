from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from ..models  import Category
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
 
    queryset=Category.objects.all().order_by('category_name')
    serializer_class= CategorySerializer
    permission_classes=[IsAuthenticated]
    
    

