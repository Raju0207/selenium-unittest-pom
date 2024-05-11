from tests.base_test import Base_Page
from selenium.webdriver.common.by import By
import time
from pages.login_page import Login_Page
from testdata.data import Data


class Login_Test(Base_Page):

    def test_login(self):
        lp = Login_Page(self.driver)
        lp.enter_user_name(Data.USERNAME)
        time.sleep(1)
        lp.enter_password(Data.PASSWORD)
        time.sleep(1)
        lp.click_on_submit_button()
        time.sleep(2)
        lp.verify_system_can_login_successfully()
        lp.click_on_burger_menu()
        time.sleep(2)
        lp.click_on_logout_button()
        time.sleep(2)

    def test_invalid_login_with_blank(self):
        bl = Login_Page(self.driver)
        bl.enter_blank_user_name(Data.USERNAME1)
        time.sleep(1)
        bl.enter_blank_password(Data.PASSWORD1)
        time.sleep(1)
        bl.click_on_submit_button()
        time.sleep(2)
        bl.verify_system_cannot_login()

        # self.driver.find_element(By.ID, 'user-name').send_keys('')
        # self.driver.find_element(By.ID, 'password').send_keys('')
        # self.driver.find_element(By.ID, 'login-button').click()
        # time.sleep(10)
        # textValue = self.driver.find_element(By.XPATH, '//h3').text
        # assert textValue == 'Epic sadface: Username is required'
        # time.sleep(5)
        # print(textValue)

    def test_invalid_login_with_wrong_user_name(self):
        wul = Login_Page(self.driver)
        wul.enter_wrong_user_name(Data.USERNAME2)
        time.sleep(1)
        wul.enter_password(Data.PASSWORD)
        time.sleep(1)
        wul.click_on_submit_button()
        time.sleep(2)
        wul.verify_system_login_with_wrong_user_name()

        # self.driver.find_element(By.ID, 'user-name').send_keys('standard')
        # self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        # self.driver.find_element(By.ID, 'login-button').click()
        # time.sleep(10)
        # textValue1 = self.driver.find_element(By.XPATH, '//h3').text
        # assert textValue1 == 'Epic sadface: Username and password do not match any user in this service'
        # time.sleep(5)
        # print(textValue1)

    def test_invalid_login_with_wrong_password(self):
        wpl = Login_Page(self.driver)
        wpl.enter_user_name(Data.USERNAME)
        time.sleep(1)
        wpl.enter_wrong_password(Data.PASSWORD2)
        time.sleep(1)
        wpl.click_on_submit_button()
        time.sleep(2)
        wpl.verify_system_login_with_wrong_password()

        # self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        # self.driver.find_element(By.ID, 'password').send_keys('secret')
        # self.driver.find_element(By.ID, 'login-button').click()
        # time.sleep(10)
        # textValue2 = self.driver.find_element(By.XPATH, '//h3').text
        # assert textValue2 == 'Epic sadface: Username and password do not match any user in this service'
        # time.sleep(5)
        # print(textValue2)
