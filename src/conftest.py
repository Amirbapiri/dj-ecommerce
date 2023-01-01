pytest_plugins = [
    "ecommerce.tests.fixtures",
    "ecommerce.tests.selenium",
    "ecommerce.tests.factories",
    "ecommerce.tests.inventory_fixtures",
    "ecommerce.tests.api_client",
    "ecommerce.tests.promotion_fixtures",
    "celery.contrib.pytest",
]
