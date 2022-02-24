from .models import Cart,CartItems


def cart_products(request):
    cart_id = request.session.session_key
    cart_item = CartItems.objects.all().filter(cart__cart_id=cart_id)
    print(cart_item)
    p=[]
    for c in cart_item:
        p.append(c.product.id)
    a=dict(cart=p)
    print(a.items())
    return dict(cart=p)

