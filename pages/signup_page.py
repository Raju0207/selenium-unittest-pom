import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


class SignUp_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def enter_email(self):
        self.insert_data(self.locator.email, "sitting-possibly@4ahr8l6e.mailosaur.net")

    def click_on_continue(self):
        self.click_element(self.locator.continue_button)

    def enter_otp(self, otp):
        for digit in range(1, 7):
            digit = int(digit)
            self.insert_data(self.locator.otp_digit(self, serial=digit), otp[digit - 1])

    def set_pin(self, pin):
        for digit in range(1, 5):
            digit = int(digit)
            self.insert_data(self.locator.set_pin_locator(self, serial=digit), pin[digit - 1])

    def set_confirm_pin(self, pin):
        for digit in range(1, 5):
            digit = int(digit)
            self.insert_data(self.locator.set_confirm_pin_locator(self, serial=digit), pin[digit - 1])

    def enter_company_name(self):
        self.insert_data(self.locator.companyName, "ABC")

    def click_on_freelancer(self):
        self.click_element(self.locator.whyYouChoose)
