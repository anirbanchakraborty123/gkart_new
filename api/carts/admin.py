from django.contrib import admin
from .models import Cart, CartItems
# Register your models here.

class CartAdmin(admin.ModelAdmin):

    list_display = ('id','cart_id','added_date','cart_total')

admin.site.register(Cart, CartAdmin)

class CartItemsAdmin(admin.ModelAdmin):

    list_display = ('id' , 'product' , 'get_product','cart','quantity','total')

    def get_product(self, obj):
        return obj.product.id
    get_product.short_description = 'Product_id'
    get_product.admin_order_field = 'product__id'

admin.site.register(CartItems, CartItemsAdmin)