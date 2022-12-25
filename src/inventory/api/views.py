from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from inventory.models import Category, Product, ProductInventory
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductInventorySerializer,
)


class CategoryList(APIView):
    def get(self, request, *args, **kwargs):
        qs = Category.objects.all()
        serializer = CategorySerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductByCategory(APIView):
    def get(self, request, category=None):
        qs = Product.objects.filter(category__slug=category)
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductInventoryByWebID(APIView):
    def get(self, request, web_id=None):
        qs = ProductInventory.objects.get(product__web_id__iexact=web_id)
        serializer = ProductInventorySerializer(qs, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
