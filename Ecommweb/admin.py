from django.contrib import admin
from .models import Category,Product,Order,OrderItem

# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display= ['title','category','slug','price','created_on']
    prepopulated_fields ={"slug":("title",)}



admin.site.register(Category)
admin.site.register(Product,MyAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
