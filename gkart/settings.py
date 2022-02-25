"""
Django settings for gkart project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from pathlib import Path

from decouple import config # For python-decouple env file

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', 'u4ez)-^+gimz=5r32p9gn-r0jm#n0tqy_$t*08jbm(tu-f(u^b') 

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG',default=False, cast=bool) 
DEBUG = True

ALLOWED_HOSTS = ['gkartenvtest.eba-fd5jmdgf.us-west-2.elasticbeanstalk.com','127.0.0.1']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.category',
    'api.accounts',
    'api.store',
    'rest_framework',
    'rest_framework.authtoken',
    'api.category.c_api',
    'api.store.s_api',
    'api.accounts.auth_api',
    'api',
    'api.carts',


]

REST_FRAMEWORK = {
#           # Use Django's standard `django.contrib.auth` permissions,
#           # or allow read-only access for unauthenticated users.
           'DEFAULT_PERMISSION_CLASSES': [
                #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
                      #  'rest_framework.permissions.IsAuthenticated',

           ],

           'DEFAULT_AUTHENTICATION_CLASSES': 
           [
                 'rest_framework.authentication.BasicAuthentication',
                 'rest_framework.authentication.SessionAuthentication',
                 'rest_framework.authentication.TokenAuthentication',  
                 # MANUALLY ADDED BECAUSE WE ARE GOING TO USE CUSTOM LOGIN AUTHENTICATION NOT DJANGOS 
           ] 
         }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',


]

ROOT_URLCONF = 'gkart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'api.category.context_processors.all_category',
                'api.carts.context_processors.cart_products'
            ],
        },
    },
]


WSGI_APPLICATION = 'gkart.wsgi.application'

AUTH_USER_MODEL= 'accounts.Account' # ADDED TO LET KNOW THAT WE WILL USE THIS 
                                    # CUSTOM USER MANAGER TO SETUP NEW USER

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
    
        'default': {
            'ENGINE':'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],                     
            'USER': os.environ['RDS_USERNAME'] ,
            'PASSWORD': os.environ['RDS_PASSWORD'] ,
            'HOST': os.environ['RDS_HOSTNAME'] ,
            'PORT': os.environ['RDS_PORT'] ,
        }
    }
else:
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR/'db.sqlite3',                     
            
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'static'
STATICFILES_DIRS=[
    'gkart/static'
]

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR/'media'


CACHE_TTL = 60 * 15

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_PREFIX" : "example"
    }
}