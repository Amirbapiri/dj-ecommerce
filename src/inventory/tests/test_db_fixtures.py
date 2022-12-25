import pytest
from django.db import IntegrityError

from inventory import models
from ecommerce.tests.factories import ProductFactory


@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", True),
        (18, "trainers", "trainers", True),
        (35, "baseball", "baseball", True),
    ],
)
def test_inventory_category_dbfixture(
    db,
    db_fixture_setup,
    id,
    name,
    slug,
    is_active,
):
    result = models.Category.objects.get(
        id=id,
        name=name,
        slug=slug,
        is_active=is_active,
    )
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", True),
        ("trainers", True),
        ("baseball", True),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, slug, is_active):
    result = category_factory.create(slug=slug, is_active=is_active)

    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "45434425",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    django_db_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_uniqueness(db, product_factory):
    product = product_factory.create(web_id=123456)

    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456)


@pytest.mark.dbfixture
def old_test_inventory_db_product_insert_data(
    db,
    product_factory,
):
    new_product = product_factory.create(category=(1, 2, 3, 4, 5, 6))
    result_product_category_count = new_product.category.all().count()


#    assert "web_id_" in new_product.web_id
#    assert result_product_category_count == 6


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "7633969397",
            "934093051374",
            1,
            1,
            1,
            True,
            97.00,
            92.00,
            46.00,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "3880741573",
            "844935525855",
            1,
            8616,
            1253,
            True,
            89.00,
            84.00,
            42.00,
            929,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_inventory_dataset(
    db,
    db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_inventory_insert_data(
    db,
    product_inventory_factory,
):
    new_product = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="product type name",
        product__web_id="123456789",
        brand__name="brand name",
    )

    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "product type name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "brand name"


def test_inventory_db_producttype_insert_data(db, product_type_factory):
    new_product_type = product_type_factory.create(
        name="product type name",
    )

    assert new_product_type.name == "product type name"


def test_inventory_db_producttype_uniqueness_integrity(
    db,
    product_type_factory,
):
    product_type_factory.create(name="unique product type")

    with pytest.raises(IntegrityError):
        product_type_factory.create(name="unique product type")


def test_inventory_db_brand_insert_data(db, brand_factory):
    new_brand = brand_factory.create(name="brand name")

    assert new_brand.name == "brand name"


def test_inventory_db_brand_uniqueness_integrity(db, brand_factory):

    brand_factory.create(name="unique brand name")

    with pytest.raises(IntegrityError):
        brand_factory.create(name="unique brand name")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "pk, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            1,
            1,
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            8616,
            "images/default.png",
            "a default image solid color",
            True,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_media_dataset(
    db,
    db_fixture_setup,
    pk,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    result = models.Media.objects.get(pk=pk)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert result.is_feature == is_feature
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_media_insert_data(db, media_factory):
    new_media = media_factory.create(
        product_inventory__sku="123456789",
    )

    assert new_media.product_inventory.sku == "123456789"
    assert new_media.image == "images/default.png"
    assert new_media.alt_text == "a default image solid color"
    assert new_media.is_feature == True


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "pk, product_inventory, last_checked, units, units_sold",
    [
        (1, 1, "2021-09-04 22:14:18", 135, 0),
        (8616, 8616, "2021-09-04 22:14:18", 100, 0),
    ],
)
def test_inventory_db_stock_dataset(
    db, db_fixture_setup, pk, product_inventory, last_checked, units, units_sold
):
    stock_instance = models.Stock.objects.get(pk=pk)
    stock_last_checked = stock_instance.last_checked.strftime("%Y-%m-%d %H:%M:%S")

    assert stock_instance.product_inventory.pk == product_inventory
    assert stock_last_checked == last_checked
    assert stock_instance.units == units
    assert stock_instance.units_sold == units_sold


def test_inventory_db_stock_insert_data(db, stock_factory):
    stock = stock_factory.create(product_inventory__sku="123456789")

    assert stock.product_inventory.sku == "123456789"
    assert stock.units == 2
    assert stock.units_sold == 100


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "pk, name, description",
    [
        (1, "men-shoe-size", "men shoe size"),
    ],
)
def test_inventory_db_product_attribute_dataset(
    db,
    db_fixture_setup,
    pk,
    name,
    description,
):

    attr_instance = models.ProductAttribute.objects.get(pk=pk)

    assert attr_instance.pk == pk
    assert attr_instance.name == name
    assert attr_instance.description == description


def test_inventory_db_product_attribute_insert_data(
    db,
    product_attribute_factory,
):
    new_attr = product_attribute_factory.create()

    assert "attribute_name" in new_attr.name
    assert "attribute_description" in new_attr.description


def test_inventory_db_product_attribute_uniqueness_integrity(
    db,
    product_attribute_factory,
):
    product_attribute_factory.create(name="unique_name")

    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="unique_name")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (1, 1, 10),
    ],
)
def test_inventory_db_product_attribute_dataset(
    db,
    db_fixture_setup,
    id,
    product_attribute,
    attribute_value,
):
    result = models.ProductAttributeValue.objects.get(id=id)

    assert result.id == id
    assert result.product_attribute.id == product_attribute
    assert result.attribute_value == str(attribute_value)


def test_inventory_db_product_attribute_value_data(
    db,
    product_attribute_value_factory,
):
    new_prod_attr_val = product_attribute_value_factory.create(
        product_attribute__name="prod_attr",
    )

    assert "attribute_value" in new_prod_attr_val.attribute_value
    assert new_prod_attr_val.product_attribute.name == "prod_attr"


def test_inventory_db_insert_inventory_product_values(
    db,
    product_with_attribute_values_factory,
):
    new_inv_attribute = product_with_attribute_values_factory.create(sku="123456789")
    result = models.ProductInventory.objects.get(sku=new_inv_attribute.sku)
    count = result.attribute_values.all().count()

    assert new_inv_attribute.sku == "123456789"
    assert count == 2
