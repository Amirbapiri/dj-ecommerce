from django.urls import path, include

from .views import SearchProductInventory

urlpatterns = [
    path("<str:query>/", SearchProductInventory.as_view()),
    path("api/", include(("search.api.urls", "api"), namespace="search_api")),
]
