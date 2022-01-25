from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    
    category_name=models.CharField(max_length=50,unique=True)
    category_slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cart_image=models.ImageField(upload_to='photos/category', blank=True)
    status = models.IntegerField(default = 1,
                                   blank = True,
                                    null = True,
                                    help_text ='1->Active, 0->Inactive', # For giving hint for this field
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now, null = True, blank = True)
                                      
                                      
    def __str__(self):
        return self.category_name
    
    #It returns links/urls for every category
    def get_url(self):
        return reverse('products_by_category', args=[self.category_slug])
    
    #THIS IS USED TO SET MODEL NAME IN DJANGO ADMIN SITE in plural or singular form
    #by deafult django add 's' at the end of the model name in django admin tmake it plural
    #for ex: for category model, django shows 'categorys' in admin but its an unappropiate word
    #        for product model, django shows 'products' in admin    
    class Meta:
        #db_table = ''
        verbose_name = 'Category' #for specifying whhich model name
        verbose_name_plural = 'Categories' # setting plural form of model name to show in admin

<<<<<<< HEAD:api/category/models.py
  
=======
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
>>>>>>> main:category/models.py
