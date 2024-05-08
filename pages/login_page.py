import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


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

    def enter_user_name(self, username):
        # self.driver.find_element(*self.locator.userName).send_keys(username)
        self.enter_at(self.locator.userName, username)

    def enter_password(self, password):
        # self.driver.find_element(*self.locator.password).send_keys(password)
        self.enter_at(self.locator.password, password)

    def click_on_submit_button(self):
        # self.driver.find_element(*self.locator.submitButton).click()
        self.click_element(self.locator.submitButton)

    def verify_system_can_login_successfully(self):
        # textValue = self.driver.find_element(*self.locator.swagLabsText).text
        textValue = self.get_text(self.locator.swagLabsText)
        assert textValue == 'Swag Labs'

    def click_on_burger_menu(self):
        self.driver.find_element(*self.locator.burgerMenu).click()

    def click_on_logout_button(self):
        self.driver.find_element(*self.locator.logoutButton).click()
