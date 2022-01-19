from .models import Category

# We are making this context_preprocessor file so that 
# we can access these functions globally in our any templates files

def menu_links(request): # This method is used to return all the categories to be used in templates
    links=Category.objects.all()
    return dict( links=links )