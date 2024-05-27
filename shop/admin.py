from django.contrib import admin
from .models import Category, Product, Order

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')

class AdminOrder(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'state', 'order_date')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)