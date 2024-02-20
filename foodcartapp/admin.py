from django.contrib import admin

from foodcartapp.models import Order, Cake


class CakeInline(admin.TabularInline):
    model = Cake
    fields = ['level', 'form', 'topping', 'berries', 'decor', 'words', 'comment']
    extra = 0


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [CakeInline]


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    pass



