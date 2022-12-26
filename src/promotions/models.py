from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.expressions import Decimal
from django.forms import ValidationError
from django.utils.text import gettext_lazy as _

from inventory.models import ProductInventory


class PromotionType(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    name = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=20)

    def __str__(self):
        return self.coupon_code


class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    promotion_reduction = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_schedule = models.BooleanField(default=False)
    promo_start = models.DateField()
    promo_end = models.DateField()
    promo_type = models.ForeignKey(
        PromotionType,
        related_name="promotion",
        on_delete=models.PROTECT,
    )
    coupon = models.ForeignKey(
        Coupon,
        related_name="promotion",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    products_on_promotion = models.ManyToManyField(
        ProductInventory,
        through="ProductOnPromotion",
        related_name="promotions",
    )

    def clean(self):
        if self.promo_start > self.promo_end:
            raise ValidationError(_("End date before the start date"))
        return super().clean()

    def __str__(self):
        return self.name


class ProductOnPromotion(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="product_on_promotion",
        on_delete=models.CASCADE,
    )
    promotion = models.ForeignKey(
        Promotion,
        related_name="product_on_promotion",
        on_delete=models.CASCADE,
    )
    promo_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    price_override = models.BooleanField(default=False)

    class Meta:
        unique_together = ("product_inventory", "promotion")
