import os
import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


class Profile_Management_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def click_on_setting(self):
        self.click_element(self.locator.settings)

    def upload_photo(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "images/photo.jpeg"))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        file_input = self.driver.find_element(By.ID, self.locator.photo)
        file_input.send_keys(upload_file)

    def enter_name(self):
        self.insert_data(self.locator.name, "Jhon")

    def click_on_save_changes(self):
        self.click_element(self.locator.save_button)
