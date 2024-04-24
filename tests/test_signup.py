import utils.utils
from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.signup_page import SignUp_Page
from testdata.test_data import TestData


class SignUp_Test(Base_Page):

    def test_signup(self):
        lp = SignUp_Page(self.driver)
        lp.enter_email()
        lp.click_on_continue()
        time.sleep(30)
        otp = utils.utils.get_otp_from_mail()
        lp.enter_otp(otp)
        time.sleep(10)