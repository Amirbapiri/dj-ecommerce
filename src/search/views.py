from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from elasticsearch_dsl import Q

from inventory.api.serializers import ProductInventorySerializer
from search.documents import ProductInventoryDocument


class SearchProductInventory(APIView, LimitOffsetPagination):
    product_inventory_serializer = ProductInventorySerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q(
                "multi_match",
                query=query,
                fields=[
                    "product.name",
                ],
                fuzziness="auto",
            ) & Q(
                "bool",
                should=[Q("match", is_default=True)],
                minimum_should_match=1,
            )

            search = self.search_document.search().query(q)
            search_response = search.execute()

            result = self.paginate_queryset(search_response, request, view=self)
            serializer = self.product_inventory_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return response.Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
