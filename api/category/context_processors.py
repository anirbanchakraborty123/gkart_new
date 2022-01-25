<<<<<<< HEAD:api/category/context_processors.py

from .models import Category


def all_category(request):
    cate= Category.objects.all()
    return dict(category=cate)
=======
from .models import Category

# We are making this context_preprocessor file so that 
# we can access these functions globally in our any templates files

def menu_links(request): # This method is used to return all the categories to be used in templates
    links=Category.objects.all()
    return dict( links=links )
>>>>>>> main:category/context_processors.py
