# Generated by Django 4.1.3 on 2022-12-08 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_brand_producttype_productinventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
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
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="format: required, default-default.png",
                        upload_to="images/",
                        verbose_name="product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        verbose_name="alternative text",
                    ),
                ),
                (
                    "is_feature",
                    models.BooleanField(
                        default=False,
                        help_text="format: default=false, true=default image",
                        verbose_name="product default image",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date media created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date media updated",
                    ),
                ),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="medias",
                        to="inventory.productinventory",
                    ),
                ),
            ],
            options={
                "verbose_name": "product image",
                "verbose_name_plural": "product images",
            },
        ),
    ]
