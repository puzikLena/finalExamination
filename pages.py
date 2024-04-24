import yaml
from selenium.webdriver.common.by import By

with open("./test_data.yaml") as f:
    test_data = yaml.safe_load(f)


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.address = test_data["address"]

    def open_site(self):
        self.driver.get(self.address)

    def find_element_by_xpath(self, xpath: str):
        return self.driver.find_element(By.XPATH, xpath)


class MainPage(Page):
    def click_on_about(self):
        self.find_element_by_xpath(test_data["about_button_xpath"]).click()


class AboutPage(Page):
    def get_about_header(self):
        return self.find_element_by_xpath(test_data["about_header_xpath"])


class AuthPage(Page):

    def input_username(self, username):
        self._input_data_to_field(test_data["username_xpath"], username)

    def input_password(self, password):
        self._input_data_to_field(test_data["password_xpath"], password)

    def click_on_login(self):
        self.find_element_by_xpath(test_data["login_button_xpath"]).click()

    def _input_data_to_field(self, xpath, data):
        field = self.find_element_by_xpath(xpath)
        field.clear()
        field.send_keys(data)

# About -  a class=svelte-1rc85o5
