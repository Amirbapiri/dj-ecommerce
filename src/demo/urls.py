from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category, name="categories"),
    path(
        "categories/<slug:category_slug>/products/",
        views.product_by_category,
        name="product_by_category",
    ),
    path(
        "products/<slug:product_slug>/",
        views.product_detail,
        name="product_detail",
    ),
]
