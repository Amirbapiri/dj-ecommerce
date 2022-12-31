from django.contrib import admin

from promotions.models import Promotion, PromotionType, ProductOnPromotion, Coupon
from promotions.tasks import promotion_prices


class ProductOnPromotionInline(admin.TabularInline):
    # model = Promotion.products_on_promotion.through
    model = ProductOnPromotion
    raw_id_fields = ("product_inventory",)


@admin.register(Promotion)
class PromotionsModelAdmin(admin.ModelAdmin):
    inlines = (ProductOnPromotionInline,)
    list_display = [
        "name",
        "promo_type",
        "is_active",
        "promo_start",
        "promo_end",
    ]

    def save_model(self, request, obj, form, change):
        promotion_prices.delay(obj.promotion_reduction, obj)
        return super().save_model(request, obj, form, change)


admin.site.register(PromotionType)
admin.site.register(Coupon)
admin.site.register(ProductOnPromotion)
