import utils.utils
from pages.profile_management_page import Profile_Management_Page
from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.login_page import Login_Page
from testdata.test_data import TestData


class LogIn_Test(Base_Page):

    def test_login(self):
        lp = Login_Page(self.driver)
        lp.click_on_login_link()
        time.sleep(2)
        lp.enter_email()
        time.sleep(2)
        lp.click_on_continue()
        time.sleep(20)
        otp = utils.utils.get_otp_from_mail()
        lp.enter_otp(otp)
        time.sleep(10)
        pmp = Profile_Management_Page(self.driver)
        pmp.click_on_setting()
        pmp.upload_photo()
        time.sleep(10)
        pmp.enter_name()
        time.sleep(20)
        pmp.click_on_save_changes()
        time.sleep(10)
        pmp.click_on_balance_change()
        time.sleep(10)
        pmp.select_balance_currency()
        time.sleep(5)
        pmp.click_on_save_button()
        time.sleep(5)