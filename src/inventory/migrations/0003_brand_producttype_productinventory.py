# Generated by Django 4.1.3 on 2022-12-06 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, unique, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="brand name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, unique, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="type of product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="format: required, unique, max-20",
                        max_length=20,
                        unique=True,
                        verbose_name="stock keeping unit",
                    ),
                ),
                (
                    "upc",
                    models.CharField(
                        help_text="format: required, unique, max-12",
                        max_length=12,
                        unique=True,
                        verbose_name="universal product code",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=product visible",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "retail_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99"
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="product retail price",
                    ),
                ),
                (
                    "store_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99"
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="product store price",
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999.99"
                            }
                        },
                        help_text="format: maximum price 999.99",
                        max_digits=5,
                        verbose_name="sale price",
                    ),
                ),
                ("weight", models.FloatField(verbose_name="product weight")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date sub-product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date sub-product updated",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="inventory.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="inventory.product",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="inventory.producttype",
                    ),
                ),
            ],
        ),
    ]
