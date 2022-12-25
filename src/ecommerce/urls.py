from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include(("demo.urls", "demo"), namespace="demo")),
    path("search/", include(("search.urls", "search"), namespace="search")),
    path("inventory/", include(("inventory.urls", "inventory"), namespace="inventory")),
]
