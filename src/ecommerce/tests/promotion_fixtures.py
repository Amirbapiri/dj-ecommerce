import pytest
from datetime import date, timedelta

from promotions.models import Promotion, PromotionType, Coupon


@pytest.fixture
def single_promotion_type(db):
    promotion_type = PromotionType.objects.create(name="promotype")
    return promotion_type


@pytest.fixture
def coupon(db):
    coupon = Coupon.objects.create(name="coupon", coupon_code="987654321")
    return coupon


@pytest.fixture
def promotion_multi_variant(
    db,
    single_promotion_type,
    coupon,
    single_sub_product_with_media_and_attributes,
):
    promotion = Promotion.objects.create(
        name="promotion",
        description="description",
        promotion_reduction=50,
        is_active=False,
        is_schedule=True,
        promo_type=single_promotion_type,
        coupon=coupon,
        promo_start=date.today(),
        promo_end=date.today() + timedelta(4),
    )

    # Adding the product to the promotion
    sub_inventory_product = single_sub_product_with_media_and_attributes["inventory"]
    promotion.products_on_promotion.add(
        sub_inventory_product,
        through_defaults={"promo_price": "100.00"},
    )

    return promotion
