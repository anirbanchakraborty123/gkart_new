from distutils.command.upload import upload
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from api.category.models import Category



# Create your models here.
class Product(models.Model):


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

    # It returns the links/url of the product_details page for a particular product
    def get_url(self):
        return reverse('product_details', args=[self.category.category_slug,self.slug])

    # For adding particular item to cart by passing product_id
    def cart_get_url(self):
        return reverse('add_to_cart', args=[self.id])

class ProductGallery(models.Model):
    product = models.ForeignKey(Product , default=None, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name ='product_gallery'
        verbose_name_plural ="Product__Gallery"