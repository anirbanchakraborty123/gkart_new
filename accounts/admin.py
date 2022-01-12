from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):

    list_display=('email','is_active','date_joined')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

    ordering=('date_joined',)

admin.site.register(Account,AccountAdmin)