class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def insert_data(self, locator, data):
        self.get_element(locator).send_keys(data)

    def get_text(self, locator):
        return self.get_element(locator).text
