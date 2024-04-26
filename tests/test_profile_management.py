import utils.utils
from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.profile_management_page import Profile_Management_Page
from testdata.test_data import TestData


class Profile_Management_Test(Base_Page):

    def test_profile_management(self):
        lp = Profile_Management_Page(self.driver)
        lp.click_on_setting()
        lp.upload_photo()
        time.sleep(10)
        lp.enter_name()
        time.sleep(20)
        lp.click_on_save_changes()
        time.sleep(10)
        lp.click_on_balance_change()
        time.sleep(10)
        lp.select_balance_currency()
        time.sleep(5)
        lp.click_on_save_button()
        time.sleep(5)