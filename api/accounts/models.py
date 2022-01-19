from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    
    def Create_user(self,first_name,last_name,username,email,password=None):
        
        if not email:
             raise ValueError('User must have an valid email address')
        
        if not username:
            raise ValueError('User must have a username')
         
        user=self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self,first_name,last_name,password,email,username):
       
        user=self.Create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
            )
        
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    
    first_name         =        models.CharField(max_length=50)
    last_name         =        models.CharField(max_length=50)
    username      =        models.CharField(max_length=50,  unique= True)
    email         =        models.EmailField(max_length=50, unique= True)
    phoneno       =        models.CharField(max_length=10)
    
    #required fields
    
    date_joined   =       models.DateTimeField(auto_now_add=True)
    last_login    =       models.DateTimeField(auto_now_add=True)
    
    #required permissions
    
    is_admin      =       models.BooleanField(default=False)
    is_staff      =       models.BooleanField(default=False)
    is_superuser  =       models.BooleanField(default=False)
    is_active     =       models.BooleanField(default=False)
    
    # For login using email  rather then username 
    
    USERNAME_FIELD='email'
    
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    objects=MyAccountManager() # To use the myaccountmanager as the setup for new account
    
    def __str__(self):
        return self.email
    
    # this function returns = the user has all the modify/edit permissions and the user is: admin
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True