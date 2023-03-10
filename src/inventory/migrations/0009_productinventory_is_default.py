# Generated by Django 4.1.3 on 2022-12-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0008_productattributevalues_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productinventory",
            name="is_default",
            field=models.BooleanField(
                default=False,
                help_text="format: true=sub product visible",
                verbose_name="default selection",
            ),
        ),
    ]
