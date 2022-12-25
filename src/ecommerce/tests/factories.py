import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from inventory import models

faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    # name = fake.lexify(text="cat_name_??????")
    name = factory.Sequence(lambda n: f"cat_slug_{n}")
    slug = faker.lexify(text="cat_slug_??????")


class ManyToManyPostGeneration(factory.PostGeneration):
    def __init__(self, name):
        def func(self, create, extracted, **kwargs):
            if create and not extracted:
                getattr(self, name).set(extracted)

        func.__name__ = name
        return super().__init__(name)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    # if you're going to use build you need to specify an 'id'
    # id = factory.Sequence(lambda n: n)
    web_id = factory.Sequence(lambda n: f"web_id_{n}")
    slug = faker.lexify(text="prod_slug_??????")
    name = faker.lexify(text="prod_name_??????")
    # category = ManyToManyPostGeneration("category")
    description = faker.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: f"type_{n}")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: f"brand_{n}")


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: f"sku_{n}")
    upc = factory.Sequence(lambda n: f"upc_{n}")
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = True
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987


class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    image = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = True


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttribute

    name = factory.Sequence(lambda n: f"attribute_name_{n}")
    description = factory.Sequence(lambda n: f"attribute_description_{n}")


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = faker.lexify(text="attribute_value_??????")


class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValues

    attributevalues = factory.SubFactory(ProductAttributeValueFactory)
    productinventory = factory.SubFactory(ProductInventoryFactory)


class ProductWithAttributeValuesFactory(ProductInventoryFactory):
    attributevalues1 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )
    attributevalues2 = factory.RelatedFactory(
        ProductAttributeValuesFactory,
        factory_related_name="productinventory",
    )


register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(MediaFactory)
register(StockFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
register(ProductAttributeValuesFactory)
register(ProductWithAttributeValuesFactory)
