from inventory.models import Category


def test_create_category(single_category):
    new_category = single_category
    category = Category.objects.first()

    assert new_category.pk == category.pk
    assert new_category.name == category.name
    assert new_category.slug == category.slug


def test_create_parent_category_with_child(category_with_child):
    new_category = category_with_child

    parent_category = Category.objects.first()

    assert parent_category.children.first() == new_category
    assert parent_category.children.first().name == new_category.name
    assert parent_category.children.first().slug == new_category.slug
