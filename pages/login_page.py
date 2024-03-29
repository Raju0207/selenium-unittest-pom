import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
# from pages.base_page import Base_Page


class Login_Page():

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def login_to_application(self):
        self.driver.find_element(*self.locator.userName).send_keys('standard_user')
        time.sleep(5)
        self.driver.find_element(*self.locator.password).send_keys('secret_sauce')
        self.driver.find_element(*self.locator.submitButton).click()

    def enter_user_name(self):
        self.driver.find_element(*self.locator.userName).send_keys('standard_user')

    def enter_password(self):
        self.driver.find_element(*self.locator.password).send_keys('secret_sauce')

    def click_on_submit_button(self):
        self.driver.find_element(*self.locator.submitButton).click()

    def verify_system_can_login_successfully(self):
        textValue = self.driver.find_element(*self.locator.swagLabsText).text
        assert textValue == 'Swag Labs'

    def click_on_burger_menu(self):
        self.driver.find_element(*self.locator.burgerMenu).click()

    def click_on_logout_button(self):
        self.driver.find_element(*self.locator.logoutButton).click()
