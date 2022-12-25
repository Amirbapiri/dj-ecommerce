from django.urls import path, include


urlpatterns = [
    path("api/", include(("inventory.api.urls", "api"), namespace="inventory_api")),
]
