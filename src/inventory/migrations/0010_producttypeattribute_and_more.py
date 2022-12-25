# Generated by Django 4.1.3 on 2022-12-13 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0009_productinventory_is_default"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductTypeAttribute",
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
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_type_attributes",
                        to="inventory.productattribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_type_attributes",
                        to="inventory.producttype",
                    ),
                ),
            ],
            options={
                "unique_together": {("product_attribute", "product_type")},
            },
        ),
        migrations.AddField(
            model_name="producttype",
            name="product_attribute_values",
            field=models.ManyToManyField(
                related_name="product_types",
                through="inventory.ProductTypeAttribute",
                to="inventory.productattribute",
            ),
        ),
    ]
