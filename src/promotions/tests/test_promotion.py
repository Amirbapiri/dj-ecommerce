from promotions.models import (
    PromotionType,
    ProductOnPromotion,
    Promotion,
    Coupon,
)


def test_single_promotion(promotion_multi_variant):
    promotion_fixture = promotion_multi_variant
    first_promotion_instance = Promotion.objects.all().first()

    assert first_promotion_instance.pk == promotion_fixture.pk
    assert (
        first_promotion_instance.coupon.coupon_code
        == promotion_fixture.coupon.coupon_code
    )
