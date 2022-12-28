from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    name = models.CharField(verbose_name=_("category name"), max_length=100)
    slug = models.SlugField(
        verbose_name=_("category safe URL"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(
        verbose_name=_("product website ID"),
        max_length=50,
        unique=True,
        help_text=_("format: required, unique"),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        verbose_name=_("product safe URL"),
        help_text=_("format: required, letters, numbers, underscores or hyphens"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        verbose_name=_("product description"),
        help_text=_("format: required"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("type of product"),
        help_text=_("format: required, unique, max-255"),
    )
    product_attribute_values = models.ManyToManyField(
        "ProductAttribute",
        related_name="product_types",
        through="ProductTypeAttribute",
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("brand name"),
        help_text=_("format: required, unique, max-255"),
    )

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    sku = models.CharField(
        verbose_name=_("stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
        max_length=20,
        unique=True,
    )
    upc = models.CharField(
        verbose_name=_("universal product code"),
        help_text=_("format: required, unique, max-12"),
        max_length=12,
        unique=True,
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    brand = models.ForeignKey(
        Brand,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    attribute_values = models.ManyToManyField(
        "ProductAttributeValue",
        related_name="product_inventory",
        through="ProductAttributeValues",
    )
    is_active = models.BooleanField(
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
        default=True,
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name=_("default selection"),
        help_text=_("format: true=sub product visible"),
    )
    retail_price = models.DecimalField(
        verbose_name=_("product retail price"),
        help_text=_("format: maximum price 999.99"),
        max_digits=10,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99"),
            }
        },
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    store_price = models.DecimalField(
        verbose_name=_("product store price"),
        help_text=_("format: maximum price 999.99"),
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99"),
            }
        },
    )
    weight = models.FloatField(
        verbose_name=_("product weight"),
    )
    created_at = models.DateTimeField(
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("date sub-product updated"),
        help_text=_("format: Y-m-d H:M:S"),
        auto_now=True,
    )

    class Meta:
        verbose_name_plural = "Product Inventories"

    def __str__(self):
        return self.product.name


class Media(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="medias",
    )
    image = models.ImageField(
        verbose_name=_("product image"),
        help_text=_("format: required, default-default.png"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        max_length=255,
        verbose_name=_("alternative text"),
        help_text=_("format: required, max-255"),
    )
    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("product default image"),
        help_text=_("format: default=false, true=default image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date media created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_("date media updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class Stock(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="stock",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("inventory stock last check date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )
    units = models.IntegerField(
        default=0,
        verbose_name=_("units/qty of stock"),
        help_text=_("format: required, default-0"),
    )
    units_sold = models.IntegerField(
        default=0,
        verbose_name=_("units sold to date"),
        help_text=_("format: required, default-0"),
    )

    class Meta:
        verbose_name = _("product stock")
        verbose_name_plural = _("product stocks")


class ProductAttribute(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("product attribute name"),
        help_text=_("format: required, unique, max-255"),
    )

    description = models.TextField(
        verbose_name=_("product attribute description"),
        help_text=_("format: required"),
    )

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="attribute_values",
        on_delete=models.CASCADE,
    )
    attribute_value = models.CharField(
        max_length=255,
        verbose_name=_("product attribute value"),
        help_text=_("format: required text or number, max-255"),
    )

    def __str__(self):
        return (
            f"prod. attr.: {self.product_attribute.name}, val.: {self.attribute_value}"
        )


class ProductAttributeValues(models.Model):
    """
    product attribute values link model
    """

    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        "ProductInventory",
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = ("attributevalues", "productinventory")


class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.PROTECT,
        related_name="product_type_attributes",
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name="product_type_attributes",
    )

    class Meta:
        unique_together = (("product_attribute", "product_type"),)
