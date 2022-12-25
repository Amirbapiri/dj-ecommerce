import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    provides a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    service = Service("/home/amir/PycharmProjects/ecommerce-v2/chromedriver")
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.close()
