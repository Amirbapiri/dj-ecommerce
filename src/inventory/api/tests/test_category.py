from django.urls import reverse_lazy


def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = reverse_lazy("inventory:inventory_api:category_list")
    response = api_client().get(endpoint)

    assert response.status_code == 200
