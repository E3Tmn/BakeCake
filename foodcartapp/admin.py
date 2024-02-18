from django.contrib import admin

from foodcartapp.models import Order, Cake


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    pass

