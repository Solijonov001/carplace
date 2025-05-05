from django.contrib import admin

# Register your models here.
from .models import Car, Brand



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name','price','year','gear_type','distance_convered')
    list_filter = ('brand','gear_type')
    search_fields = ('name','description')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','logo')
    search_fields = ('name','description')








