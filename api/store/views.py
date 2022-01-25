from django.shortcuts import render,get_object_or_404
from .models import Product
from api.category.models import Category
# Create your views here.
def store(request, category_slug= None):

      categories = None
      products= None

      if category_slug != None:
            categories= get_object_or_404(Category, category_slug=category_slug)
            products= Product.objects.filter(category=categories,is_available= True)
            products_count= products.count()
      else:    
            products  = Product.objects.all().filter(is_available=True)
            products_count= products.count() #for geting all total no of products

      #products_count= Product.objects.all().filter(is_available=True).count()
      #OR products_count= products.count()


      context={
               'products': products,
               'p_count' : products_count,
                           }
      return render(request, 'store/store.html', context)

def product_details(request, category_slug, product_slug):
      try:
            product= Product.objects.get(category__category_slug = category_slug, slug=product_slug)
           
      except Exception as e:
            raise e
      context={
            'single_product': product
      }
      return render(request, 'store/product_detail.html',context)