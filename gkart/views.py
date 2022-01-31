from functools import _CacheInfo
from django.shortcuts import render
from api.store.models import Product
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache, caches
from django.db.models import Q


CACHE_TTL = getattr(settings, 'CACHE_TTL' , DEFAULT_TIMEOUT) 

def home(request):
        
    products  = Product.objects.all().filter(is_available=True)
    context={
               'products': products
            }

    return render(request, 'home.html', context)


def search_product(request):

    search=request.POST.get("search" , None)
    try:
            if cache.get(search):
                products = cache.get(search)
                print("FROM CACHE")
                print(cache.get(search))
            else:
                if search:
                    products = Product.objects.all().filter(Q(is_available=True) & Q(product_name__contains= search) | Q(category__category_name__contains= search))
                    cache.set(search, products) 
                    print("FROM DB")
                    print(cache.get(search))
                else:
                    products  = Product.objects.all().filter(Q(is_available=True) & Q(product_name__contains= search) | Q(category__category_name__contains= search))
    except:
            products  = Product.objects.all().filter(Q(is_available=True) & Q(product_name__contains= search) | Q(category__category_name__contains= search))

    products_count= products.count()    
    context={
               'products': products,
               'search'  : search,
               'p_count' : products_count

            }

    return render(request, 'store/store.html', context)




