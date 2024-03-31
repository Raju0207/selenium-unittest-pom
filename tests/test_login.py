from base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.login_page import Login_Page
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

    def test_invalid_login_with_wrong_username(self):
        lp = Login_Page(self.driver)
        lp.enter_user_name('standard_userjhsdbfjk')
        time.sleep(1)
        lp.enter_password('secret_sauce')
        time.sleep(1)
        lp.click_on_submit_button()
        time.sleep(2)
        lp.verify_system_cannot_login_successfully_for_wrong_password()
        time.sleep(5)

    def test_invalid_login_with_wrong_user_name(self):
        lp = Login_Page(self.driver)
        lp.enter_user_name('standard_user')
        time.sleep(1)
        lp.enter_password('secret_saucejgvh')
        time.sleep(1)
        lp.click_on_submit_button()
        time.sleep(2)
        lp.verify_system_cannot_login_successfully()
        time.sleep(5)

    # def test_invalid_login_with_wrong_password(self):
    #     self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    #     self.driver.find_element(By.ID, 'password').send_keys('secret')
    #     self.driver.find_element(By.ID, 'login-button').click()
    #     time.sleep(10)
    #     textValue2 = self.driver.find_element(By.XPATH, '//h3').text
    #     assert textValue2 == 'Epic sadface: Username and password do not match any user in this service'
    #     time.sleep(5)
    #     print(textValue2)
