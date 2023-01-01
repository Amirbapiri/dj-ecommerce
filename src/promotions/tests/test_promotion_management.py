import pytest
from datetime import date, timedelta

from promotions.models import Promotion
from promotions.tasks import promotion_prices


@pytest.mark.parametrize("reduction, result", [(10, 90), (50, 50)])
def test_promotion_price_reduction(
    transactional_db,
    reduction,
    result,
    celery_app,
    celery_worker,
    promotion_multi_variant,
):
    promotion_prices(reduction_amount=reduction, instance=promotion_multi_variant)
    product_on_promo = Promotion.products_on_promotion.through.objects.get(
        promotion=promotion_multi_variant
    )

    assert product_on_promo.promo_price == result
