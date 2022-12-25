from django.urls import path

from .views import CategoryList, ProductByCategory, ProductInventoryByWebID

urlpatterns = [
    # Category endpoints
    path("category/all/", CategoryList.as_view(), name="category_list"),
    path(
        "category/<slug:category>/products/",
        ProductByCategory.as_view(),
        name="product_by_category",
    ),
    path(
        "product/<str:web_id>/",
        ProductInventoryByWebID.as_view(),
        name="product_inventory_by_web_id",
    ),
]
