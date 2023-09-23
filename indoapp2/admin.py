from django.contrib import admin
from indoapp2.models import Products,PlacedOrder

# Register your models here.

class Product_list(admin.ModelAdmin):
    list_display=['ProductName','ProductDetails','ProductPrice','ProductCategory','ProductImage','ProductBrand']
    
admin.site.register(Products,Product_list)

@admin.register(PlacedOrder)
class Orders_list(admin.ModelAdmin):
    list_display=['user','customer','quantity','status','ordered_date']