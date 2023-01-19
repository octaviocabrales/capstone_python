from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage

import os

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(os.getenv("BASE_URL"))

    def send_credentials(self):
        self.driver.find_element(By.ID, "user-name").send_keys(os.getenv("USER_SAUCE"))
        self.driver.find_element(By.ID, "password").send_keys(os.getenv("PASSWORD_SAUCE"))

    def click_on_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

    def is_products_page_displayed(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "header_secondary_container")
            self.driver.find_element()
        except NoSuchElementException as e: return False
        return True
