from django.contrib import admin
from .models import User, Customer
from reversion.admin import VersionAdmin



class UserAdmin(VersionAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('username',)
    search_fields = ('username', 'email')


class CustomerAdmin(VersionAdmin):
    list_display = ('name','customer', 'phone', 'location', 'full_name')
    list_filter = ('location',)
    search_fields = ('location',)

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)