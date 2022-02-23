from django.http import response,request
from django.shortcuts import redirect, render
from api.store.models import Product
from .models import Cart, CartItems

# Create your views here.

# For getting the cart_id/current session_key(and its a private function)
def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

# HOME VIEW FOR CART
def cart(request):
    return render(request, 'cart/cart.html')

# For add to cart functionality
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # For getting products using session_key/cart_id    
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
             # We are adding session_key as cart_id because it would be unique and it would uniquely identify users           
            cart_id = _cart_id(request),
            cart_total = product.price
             # IF cart_id not present then add the session_key as unique cart_id
        )
        cart.save() # Saving model cart into database/ saving a new row into CART model

    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 # To increment the quantity of the cart_product
        cart_item.total = cart_item.product.price*cart_item.quantity
        cart.cart_total += cart_item.product.price*cart_item.quantity
        cart.save()
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            cart    = cart,
            quantity= 1  ,
            total   = product.price          
        )
        cart_item.save()

    return redirect('cart')

def cart_products(request): 
    
    try:
        if(_cart_id(request)):
            carts = Cart.objects.get(cart_id=_cart_id(request))
            cart_p = CartItems.objects.all().filter(cart__cart_id=carts.cart_id)

            pr=[]
            for c in cart_p:
                s= c.product.price * c.quantity
                pr.append(s)
            cart_total = float(sum(pr))
            cart_tax   = (2*cart_total)/100
            grand_total= cart_total+cart_tax
            context={
                'cart_ps'    :  cart_p,
                'cart_total' :  cart_total,
                'cart_tax'   :  cart_tax,
                'grand_total':  grand_total
            }
        else:
            context={} 
    except  :
          context={} 

    return render(request ,'cart/cart.html', context)

    