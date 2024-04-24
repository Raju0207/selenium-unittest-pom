from pages.login_page import Login_Page
from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from testdata.test_data import TestData


class Login_Test(Base_Page):

    def test_valid_login(self):
        lp = Login_Page(self.driver)
        lp.enter_user_name(TestData.USERNAME)
        time.sleep(1)
        lp.enter_password(TestData.PASSWORD)
        time.sleep(1)
        lp.click_on_submit_button()
        time.sleep(2)
        lp.verify_system_can_login_successfully()
        lp.click_on_burger_menu()
        time.sleep(2)
        lp.click_on_logout_button()
        time.sleep(2)

