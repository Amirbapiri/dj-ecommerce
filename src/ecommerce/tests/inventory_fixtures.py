import pytest

from inventory.models import (
    Brand,
    Category,
    Product,
    ProductInventory,
    Media,
    ProductAttribute,
    ProductAttributeValue,
    ProductType,
)


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="category", slug="category")


@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name="parent", slug="parent")
    parent.children.create(name="child", slug="child")

    child = parent.children.first()
    return child


@pytest.fixture
def category_with_multiple_children(db):
    categories = Category.objects.build_tree_nodes(
        {
            "id": 1,
            "name": "parent",
            "slug": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child 1",
                    "slug": "child-1",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "child 1 2",
                            "slug": "child-1-2",
                        }
                    ],
                }
            ],
        }
    )
    category = Category.objects.bulk_create(categories)
    return category


@pytest.fixture
def single_product(db, category_with_child):
    product = Product.objects.create(
        web_id="123456789",
        slug="default",
        name="default",
        is_active=True,
    )
    product.category.add(category_with_child)
    return product


@pytest.fixture
def product_attribute(db):
    product_attribute = ProductAttribute.objects.create(
        name="product_attribute",
        description="product_attribute",
    )
    return product_attribute


@pytest.fixture
def product_type(db, product_attribute):
    product_type = ProductType.objects.create(name="product_type")
    product_type.product_attribute_values.add(product_attribute)

    return product_type


@pytest.fixture
def brand(db):
    brand = Brand.objects.create(name="brand")
    return brand


@pytest.fixture
def product_attribute_value(db, product_attribute):
    product_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=product_attribute, attribute_value="default"
    )
    return product_attribute_value


@pytest.fixture
def single_sub_product_with_media_and_attributes(
    db,
    single_product,
    product_type,
    brand,
    product_attribute_value,
):

    sub_product = ProductInventory.objects.create(
        sku="123456789",
        upc="100000000001",
        product_type=product_type,
        product=single_product,
        brand=brand,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        sale_price="9.99",
        is_active=False,
        weight=1000.0,
    )
    media = Media.objects.create(
        product_inventory=sub_product,
        image="images/default.png",
        alt_text="default",
        is_feature=True,
    )
    sub_product.attribute_values.add(product_attribute_value)

    return {
        "inventory": sub_product,
        "media": media,
        "attribute": product_attribute_value,
    }
