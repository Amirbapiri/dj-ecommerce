from datetime import datetime
from decimal import Decimal
from math import ceil

from django.db import transaction
from celery import shared_task

from .models import Promotion


@shared_task(name="apply_promotion_to_products_on_promotion")
def promotion_prices(reduction_amount, instance):
    with transaction.atomic():
        # Getting all the items included in the promotion
        products_in_promotion = Promotion.products_on_promotion.through.objects.filter(
            promotion=instance,
        )
        reduction = reduction_amount / 100

        for p in products_in_promotion:
            if not p.price_override:
                # Here is when we perform price reduction
                store_price = p.product_inventory.store_price
                reduced_store_price = ceil(
                    store_price - (store_price * Decimal(reduction)),
                )
                p.promo_price = Decimal(reduced_store_price)
                p.save()
