from rest_framework import serializers

from inventory.models import (
    Category,
    Product,
    Media,
    ProductAttributeValue,
    Brand,
    ProductType,
    ProductInventory,
)


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "web_id"]
        read_only = True
        editable = False


class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ("img_url", "alt_text")
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.image.url


class ProductInventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values",
        many=True,
        read_only=True,
    )

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
            "media",
            "is_active",
            "weight",
            "medias",
            "stock",
            "product_type",
            "attributes",
        ]
        read_only = True


class ProductInventorySearchSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = (
            "pk",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        )
