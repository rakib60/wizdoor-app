from django.contrib import admin
from .models import Product, Category
from reversion.admin import VersionAdmin



class ProductAdmin(VersionAdmin):
    list_display = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('title',)
    list_select_related = ('category',)

class CategoryAdmin(VersionAdmin):
    list_display = ('title', )
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)