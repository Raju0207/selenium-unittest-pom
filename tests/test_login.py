import utils.utils
from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.login_page import Login_Page
from testdata.test_data import TestData


class LogIn_Test(Base_Page):

    def test_login(self):
        lp = Login_Page(self.driver)
        lp.click_on_login_link()
        lp.enter_email()
        lp.click_on_continue()
        time.sleep(20)
        otp = utils.utils.get_otp_from_mail()
        lp.enter_otp(otp)
        time.sleep(10)
