from django.contrib import admin
from .models import Order, OrderItem
from reversion.admin import VersionAdmin



class OrderAdmin(VersionAdmin):
    list_display = ('customer','start_date', 'ordered_date')
    list_filter = ('customer',)
    search_fields = ('customer',)

class OrderItemAdmin(VersionAdmin):
    list_display = ('customer', 'product', 'quantity' )
    search_fields = ('customer',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)