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
        # self.driver.find_element(*self.locator.burgerMenu).click()
        self.click_element(self.locator.burgerMenu)

    def click_on_logout_button(self):
        # self.driver.find_element(*self.locator.logoutButton).click()
        self.click_element(self.locator.logoutButton)

    def enter_blank_user_name(self, username1):
        self.enter_at(self.locator.userName1, username1)

    def enter_blank_password(self, password1):
        self.enter_at(self.locator.password1, password1)

    def verify_system_cannot_login(self):
        # textValue = self.driver.find_element(*self.locator.swagLabsText).text
        textValue1 = self.get_text(self.locator.TextMessage)
        assert textValue1 == 'Epic sadface: Username is required'

    def enter_wrong_user_name(self, username2):
        # self.driver.find_element(*self.locator.userName).send_keys(username)
        self.enter_at(self.locator.userName2, username2)

    def verify_system_login_with_wrong_user_name(self):
        # textValue = self.driver.find_element(*self.locator.swagLabsText).text
        textValue2 = self.get_text(self.locator.TextMessage)
        assert textValue2 == 'Epic sadface: Username and password do not match any user in this service'

    def enter_wrong_password(self, password2):
        # self.driver.find_element(*self.locator.password).send_keys(password)
        self.enter_at(self.locator.password2, password2)

    def verify_system_login_with_wrong_password(self):
        # textValue = self.driver.find_element(*self.locator.swagLabsText).text
        textValue3 = self.get_text(self.locator.TextMessage)
        assert textValue3 == 'Epic sadface: Username and password do not match any user in this service'
