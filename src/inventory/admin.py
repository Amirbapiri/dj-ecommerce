from django.contrib import admin

from .models import Category, Product, ProductInventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(ProductInventory)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)
