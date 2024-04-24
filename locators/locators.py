from selenium.webdriver.common.by import By


class Locators:
    email = (By.ID, 'email')
    continue_button = (By.XPATH, '//button[text()="Continue"]')

    def otp_digit(self, serial):
        return By.XPATH, f'//div[@class="pincode-input-container"]/input[{serial}]'

    submitButton = (By.ID, 'login-button')
    swagLabsText = By.XPATH, '//div[@class ="app_logo"]'
    burgerMenu = By.ID, 'react-burger-menu-btn'
    logoutButton = By.ID, 'logout_sidebar_link'
    errorText = By.XPATH, '//h3'
