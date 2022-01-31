from django.db import models
from api.store.models import Product
import datetime

# Create your models here.

class Cart(models.Model):

    cart_id    = models.CharField(max_length=250, blank=True)
    added_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.cart_id 

    class Meta:
        verbose_name= 'Cart'
        verbose_name_plural= 'Carts'

class CartItems(models.Model):

    product    = models.ForeignKey(Product , on_delete= models.CASCADE)
    cart       = models.ForeignKey(Cart , on_delete= models.CASCADE)
    quantity   = models.IntegerField(default=1)
    added_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.product.product_name 

    class Meta:
        verbose_name= 'CartItem'
        verbose_name_plural= 'CartItems'