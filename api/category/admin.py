from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
        list_display = ('id','category_name', 'active', 'created_on')
        list_filter=('category_name','category_slug', 'status', 'created_on','updated_on')
        search_fields = ['category_name']   # Toshow search bar in admn page above to search selected/mentioned fields
        prepopulated_fields={'category_slug': ('category_name',)}

        def active(self, obj):
             return obj.status == 1
  
        active.boolean = True

admin.site.register(Category, CategoryAdmin)