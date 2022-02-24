from functools import _CacheInfo
from itertools import product
from django.shortcuts import render,HttpResponse
from api.store.models import Product
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache, caches
from django.db.models import Q
import json
import time
from api.carts.models import Cart,CartItems
from django.http import response,request

CACHE_TTL = getattr(settings, 'CACHE_TTL' , DEFAULT_TIMEOUT) 

def home(request):
        
    products  = Product.objects.all().filter(is_available=True)
    context={
               'products': products
            }

    return render(request, 'home.html', context)


# Search products and categories using " REDIS " cache
def search_product(request):  # sourcery skip: none-compare

    search=request.GET.get("id-search" , None)
    q =request.GET.get("search1" , " ")
    print("inside search_product")
    print(q)
    if search == None:
        search=q

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
            products  = Product.objects.all().filter(Q(is_available=True) & Q(product_name__contains= search) | Q(category__category_name__contains= search)| Q(product_name= search))

    products_count= products.count()    
    context={
               'products': products,
               'search'  : search,
               'p_count' : products_count

            }

    return render(request, 'store/store.html', context)

# Autocomplete for  jquery/ajaz call for getting the related products 
def autocomplete(request):
    # sourcery skip: assign-if-exp, extract-method, inline-immediately-returned-variable, list-comprehension, move-assign-in-block
    if request.is_ajax():
        q =request.GET.get("search1" , " ")
        print("inside autocomplete")
        print(q)
       
        search_qs = Product.objects.filter(product_name__contains=q)
        results = []
        for r in search_qs:
            results.append(r.product_name)
        data = json.dumps(results)
    else:
        data = 'None'
        #time.sleep(5)

    return HttpResponse(data)

# AJAX CALL HANDLER FOR UPDATING CART_ITEMS
def update_cart(request):
    # sourcery skip: assign-if-exp, extract-method, inline-immediately-returned-variable, list-comprehension, move-assign-in-block
    if request.is_ajax():
        quantity =request.GET.get("quantity1" , None)
        product_id =request.GET.get("product" , None)
        remove =request.GET.get("remove" , None)
        session_id  = request.session.session_key
        print(remove)
        print(session_id)
        print(quantity)
        print(product_id)
        if quantity != None and  product_id != None :
            
            # UPDATE CART_ITEMS
                cart_items = CartItems.objects.get(cart__cart_id=session_id, product__id=product_id)
                subtotal   = cart_items.product.price*int(quantity)              
                update_cartItems     = CartItems.objects.filter(cart__cart_id=session_id, product__id=product_id).update(quantity=quantity,total=subtotal)
            # END OF UPDATE CART_ITEMS    

            # UPDATE CART    
                if update_cartItems:
                        cartt      = CartItems.objects.all().filter(cart__cart_id=session_id)
                        carttotal=0
                        for c in cartt:
                                carttotal  = carttotal+c.total
                                # print(carttotal)
                        tax = (2*carttotal)/100
                        grandtotal =carttotal+tax
                        # print(grandtotal)
                        
                        update_cart= Cart.objects.filter(cart_id=session_id).update(cart_total=grandtotal)
            # END/CART UPDATED

                if update_cartItems and update_cart:
                    data='success'
                else:
                    data='fail'
        else:
            data= "fail"

        if remove != None:
                
                query = CartItems.objects.filter(cart__cart_id=session_id, product__id=remove).delete()
                
                # UPDATE CART    
                if query:
                        cartt      = CartItems.objects.all().filter(cart__cart_id=session_id)
                        carttotal=0
                        for c in cartt:
                                carttotal  = carttotal+c.total
                                # print(carttotal)
                        tax = (2*carttotal)/100
                        grandtotal =carttotal+tax
                        # print(grandtotal)
                        
                        update_cart= Cart.objects.filter(cart_id=session_id).update(cart_total=grandtotal)
            # END/CART UPDATED

                
                if(query):
                    data='success'
                else:
                    data="fail"
        else:
            print("wrongg")
    else:
        data = 'fail'
        #time.sleep(5)

    return HttpResponse(data)


def cart_details(request):
    session_id  = request.session.session_key
    cart_p   = CartItems.objects.all().filter(cart__cart_id=session_id)
    if cart_p:
            print("success cart details")
            results=[]
            for r in cart_p:
                    results.append(r.product.id)
            data = json.dumps(results)
    else:
        # print("failed cart details")
        data = "fail"
    return HttpResponse(data)
    