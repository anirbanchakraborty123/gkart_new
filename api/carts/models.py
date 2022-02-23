from django.urls import reverse
from django.db import models
from api.store.models import Product
import datetime

# Create your models here.

class Cart(models.Model):

    cart_id    = models.CharField(max_length=250, blank=True)
    added_date = models.DateTimeField(default=datetime.datetime.now)
    cart_total = models.IntegerField(default=0)

    def __str__(self):
        return self.cart_id 

        
    class Meta:
        verbose_name= 'Cart'
        verbose_name_plural= 'Carts'

class CartItems(models.Model):

    product    = models.ForeignKey(Product , on_delete= models.CASCADE, default= 0)
    cart       = models.ForeignKey(Cart , on_delete= models.CASCADE)
    quantity   = models.IntegerField(default=1)
    added_date = models.DateTimeField(default=datetime.datetime.now)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return self.product.product_name

    def sub_total(self):
        return self.product.price * self.quantity
    class Meta:
        verbose_name= 'CartItem'
        verbose_name_plural= 'CartItems'


    # def get_url(self):
    #     return reverse('add_to_cart', args=[self.product.id])