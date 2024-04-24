import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import test_data, AuthPage, MainPage, AboutPage


@pytest.fixture(scope='function')
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def login(driver):
    auth_page = AuthPage(driver)
    auth_page.open_site()
    auth_page.input_username(test_data["username"])
    auth_page.input_password(test_data["password"])
    auth_page.click_on_login()


def go_to_about(driver):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.click_on_about()


def test_login(driver):
    login(driver)
    time.sleep(3)


def test_click_on_about(driver):
    login(driver)
    time.sleep(3)

    go_to_about(driver)
    time.sleep(3)


def test_check_header_size(driver):
    login(driver)
    time.sleep(3)

    go_to_about(driver)
    time.sleep(3)

    about_page = AboutPage(driver)
    header = about_page.get_about_header()
    assert header.value_of_css_property('font-size') == '32px'
