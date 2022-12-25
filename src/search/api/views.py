from rest_framework import status, response
from rest_framework.views import APIView
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination

from inventory.api.serializers import ProductInventorySearchSerializer
from search.documents import ProductInventoryDocument


class SearchProductInventoryAPIView(APIView, LimitOffsetPagination):
    product_inventory_serializer = ProductInventorySearchSerializer
    search_els_document = ProductInventoryDocument

    def get(self, request, query, *args, **kwargs):
        try:
            els_q = Q(
                "multi_match",
                query=query,
                fields=["product.name", "product.web_id", "brand.name"],
                fuzziness="auto",
            ) & Q(
                "bool",
                should=[Q("match", is_default=True)],
                minimum_should_match=1,
            )
            search = self.search_els_document.search().query(els_q)
            search_response = search.execute()

            result = self.paginate_queryset(search_response, request, view=self)
            serializer = self.product_inventory_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return response.Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
