# Generated by Django 4.1.3 on 2022-12-31 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0012_remove_productinventory_sale_price_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productinventory",
            options={"verbose_name_plural": "Product Inventories"},
        ),
    ]
