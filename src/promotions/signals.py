from django.db.models.signals import post_save
from django.dispatch import receiver

from promotions.models import Promotion
from promotions.tasks import promotion_prices


# @receiver(post_save, sender=Promotion)
def update_products_on_promotion_price(sender, instance, created, **kwargs):
    if created:
        promotion_prices.delay(
            reduction_amount=instance.promotion_reduction,
            instance=instance,
        )
