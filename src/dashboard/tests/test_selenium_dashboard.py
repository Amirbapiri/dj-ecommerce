import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# @pytest.mark.selenium
# def test_create_new_admin_user(create_admin_user):
#     assert create_admin_user.__str__() == "admin"


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server,
    db_fixture_setup,
    chrome_browser_instance,
):
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")

    submit_btn = browser.find_element(By.XPATH, "//input[@value='Log in']")

    username.send_keys("admin")
    password.send_keys("123456")
    submit_btn.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
