from django.contrib import admin

from .models import Category, Product, ProductInventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)
    list_display = ("product", "store_price")
