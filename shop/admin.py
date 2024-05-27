from django.contrib import admin
from .models import Category, Product, Order

admin.site.site_header = "E-commerce"
admin.site.site_title = "sgbd-shop"
admin.site.index_title = "Manager"

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminOrder(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'state', 'order_date')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)