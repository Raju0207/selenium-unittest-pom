import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class Base_Page(unittest.TestCase):
    driver = None

    def setUp(self):
        service_chrome = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(120)
        print("I am running first")
        return self.driver

    def tearDown(self):
        print("I am running at the last")
        self.driver.close()
        self.driver.quit()

