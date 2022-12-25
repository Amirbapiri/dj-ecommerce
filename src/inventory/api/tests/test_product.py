import pytest
from django.urls import reverse_lazy
from rest_framework import status

from ecommerce.utils import convert_to_dot_notation


def test_get_product_by_category(api_client, single_product):
    endpoint = reverse_lazy(
        "inventory:inventory_api:product_by_category",
        kwargs={"category": single_product.category.first().slug},
    )
    response = api_client().get(endpoint)
    expected_response_json = [
        {"name": single_product.name, "web_id": single_product.web_id}
    ]

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response_json


def test_get_inventory_by_web_id(
    api_client,
    single_sub_product_with_media_and_attributes,
):

    single_sub_product = single_sub_product_with_media_and_attributes
    endpoint = reverse_lazy(
        "inventory:inventory_api:product_inventory_by_web_id",
        kwargs={"web_id": single_sub_product["inventory"].product.web_id},
    )
    response = api_client().get(endpoint)

    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_json["brand"]["name"] == "brand"
    assert response_json["is_default"] == True
