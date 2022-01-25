from django.shortcuts import render
from store.models import Product
# import logging
# log= logging.getLogger('django')


def home(request):
        
    products  = Product.objects.all().filter(is_available=True)
    # log.info('DEBUGGING LOG')
    # log.info(products)

    context={
               'products': products
            }

    return render(request, 'home.html', context)



