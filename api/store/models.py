from django.db import models
from api.category.models import Category


# Create your models here.
class Product(models.Model):


    #pr_name      =       models.CharField(max_length=200,unique=True)
    product_name  =      models.CharField(max_length=50,unique=True)
    slug         =       models.SlugField(max_length=200,unique=True)
    description  =       models.TextField(max_length=200,blank=True)
    price        =       models.IntegerField()
    images       =       models.ImageField(upload_to='photos/categories',blank=True)
    stock        =       models.IntegerField()
    is_available =       models.BooleanField(default=True)
    is_active    =       models.BooleanField(default=True)
    category     =       models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date =       models.DateTimeField(auto_now_add=True)
    modified_date=       models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.product_name

    # For rendering/loading the images  in the template/html file
    # because only product.images.url is not working in the html file
    # @property
    # def photo_url(self):
    #     if self.images and hasattr(self.images, 'url'):
    #         return self.images.url