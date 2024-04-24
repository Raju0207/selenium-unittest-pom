import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


# from pages.base_page import Base_Page


class SignUp_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def enter_email(self):
        # self.driver.find_element(*self.locator.userName).send_keys(username)
        self.insert_data(self.locator.email, "sitting-possibly@4ahr8l6e.mailosaur.net")

    def click_on_continue(self):
        self.click_element(self.locator.continue_button)

    def enter_otp(self, otp):
        # self.driver.find_element(*self.locator.password).send_keys(password)
        for digit in range(1, 7):
            digit = int(digit)
            self.insert_data(self.locator.otp_digit(self, serial=digit), otp[digit - 1])
