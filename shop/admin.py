from django.contrib import admin

from shop.models import Product


# Register your models here.




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('external_id', 'title', 'price', 'description', 'created_at', 'image')
   fields = ('external_id', 'title', 'price', 'description', 'created_at', 'image')
   readonly_fields = ('external_id', "created_at",)
   search_fields = ("title",)
