from django.shortcuts import render
<<<<<<< HEAD
from api.store.models import Product
import logging
log= logging.getLogger('django')
=======
from store.models import Product
# import logging
# log= logging.getLogger('django')
>>>>>>> main


def home(request):
        
    products  = Product.objects.all().filter(is_available=True)
    # log.info('DEBUGGING LOG')
    # log.info(products)

    context={
               'products': products
            }

    return render(request, 'home.html', context)



