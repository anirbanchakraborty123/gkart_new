from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Product
from api.category.models import Category
from api.carts.models import CartItems
from api.carts.views import _cart_id 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def store(request, category_slug= None):

      categories = None
      products= None


      if category_slug != None:
            categories= get_object_or_404(Category, category_slug=category_slug)
            products= Product.objects.filter(category=categories,is_available= True)
            paginator = Paginator(products,3)
            page = request.GET.get('page')
            page_products= paginator.get_page(page)
            products_count= products.count() #for geting all total no of products

      else:    
            products  = Product.objects.all().filter(is_available=True).order_by('id')
            paginator = Paginator(products,3)
            page = request.GET.get('page')
            page_products= paginator.get_page(page)
            products_count= products.count() #for geting all total no of products

      

      
      cart_pr = []
      session_id  = request.session.session_key
      cart_p      = CartItems.objects.all().filter(cart__cart_id=session_id)
      
      if(cart_p):
           for c in cart_p:
               cart_pr.append(c.product.id)
      else:
           cart_pr.append('0')
      context={
               'products': page_products,
               'p_count' : products_count,
               'cart_pr' : cart_pr
               
                           }
      return render(request, 'store/store.html', context)

def product_details(request, category_slug, product_slug):
      try:
            single_product= Product.objects.get(category__category_slug = category_slug, slug=product_slug)
            in_cart = CartItems.objects.filter(cart__cart_id=_cart_id(request) , product= single_product).exists()
            
      except Exception as e:
            raise e
      context={
            'single_product': single_product,
            'in_cart'       : in_cart
      }
      return render(request, 'store/product_detail.html',context)
