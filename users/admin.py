from django.contrib import admin
from users.models import  CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','first_name','last_name','is_staff')
    list_display_links = ('id','username','first_name','last_name')
    search_fields = ('username','email','first_name','last_name')

    fieldsets = (
        ('User',{'fields':('username','password','email')}),
        ('personal info',{'fields':('first_name','last_name','avatar','profession','bio')}),
        ('Perimissions',{'fields':('is_activate','is_staff','is_superuser')}),
        ('Important',{'fields':('last_logen','data_joined')}),

    )

