import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


# from pages.base_page import Base_Page


class Login_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def login_to_application(self):
        self.driver.find_element(*self.locator.userName).send_keys('standard_user')
        time.sleep(5)
        self.driver.find_element(*self.locator.password).send_keys('secret_sauce')
        self.driver.find_element(*self.locator.submitButton).click()

