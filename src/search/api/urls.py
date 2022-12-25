from django.urls import path

from search.api.views import SearchProductInventoryAPIView

urlpatterns = [
    path(
        "<str:query>/",
        SearchProductInventoryAPIView.as_view(),
        name="search_product_inventory",
    ),
]
