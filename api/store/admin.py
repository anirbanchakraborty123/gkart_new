from django.contrib import admin
from .models import Product
# Register your 
# models here.


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
        list_display = ('id','product_name','category' ,'is_active', 'created_date','price','is_available')
        list_filter=('product_name', 'category','is_active','is_available','created_date','price')
        search_fields = ['product_name']   # Toshow search bar in admn page above to search selected/mentioned fields
        prepopulated_fields={'slug': ('product_name',)}
        #sortable_by=('created_date')
        

        
  
        
admin.site.register(Product,ProductAdmin)