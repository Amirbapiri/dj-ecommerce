from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg

from inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    categories = models.Category.objects.all()

    return render(request, "categories.html", {"categories": categories})


def product_by_category(request, category_slug):
    products = models.Category.objects.get(slug=category_slug).product_set.values(
        "pk",
        "name",
        "slug",
        "category__name",
        "product_inventory__store_price",
    )
    return render(request, "products.html", {"products": products})


def product_detail(request, product_slug):
    filter_qs = []

    if request.GET:
        filter_qs = [qs for qs in request.GET.values()]

        product_inventory = (
            models.ProductInventory.objects.filter(
                product__slug=product_slug,
                attribute_values__attribute_value__in=filter_qs,
            )
            .annotate(num_tags=Count("attribute_values"))
            .filter(num_tags=len(filter_qs))
        )
    else:
        product_inventory = (
            models.ProductInventory.objects.filter(
                product__slug=product_slug,
                is_default=True,
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )

    y = (
        models.ProductInventory.objects.filter(product__slug=product_slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )

    z = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_inventory__product__slug=product_slug
        )
        .distinct()
        .values("product_attribute__name")
    )

    return render(
        request,
        "product_detail.html",
        {
            "product_inventory": product_inventory,
            "y": y,
            "z": z,
        },
    )
