from selenium.webdriver.common.by import By


class Locators:
    email = (By.ID, 'email')
    continue_button = (By.XPATH, '//button[text()="Continue"]')

    def otp_digit(self, serial):
        return By.XPATH, f'//div[@class="pincode-input-container"]/input[{serial}]'

    def set_pin_locator(self, serial):
        return By.XPATH, f'(//div[@class="pincode-input-container"])[1]/input[{serial}]'

    def set_confirm_pin_locator(self, serial):
        return By.XPATH, f'(//div[@class="pincode-input-container"])[2]/input[{serial}]'

    companyName = By.ID, 'companyName'
    whyYouChoose = By.NAME, 'question'

    login = By.XPATH, '//a[text() = "Log in"]'

    settings = By.XPATH, '//span[text() = "Settings"]'

    photo = By.XPATH, '//input[@type ="file"]'
    name = By.ID, 'name'
    save_button = By.XPATH, '//button[text() ="Save changes"]'



    # submitButton = (By.ID, 'login-button')
    # swagLabsText = By.XPATH, '//div[@class ="app_logo"]'
    # burgerMenu = By.ID, 'react-burger-menu-btn'
    # logoutButton = By.ID, 'logout_sidebar_link'
    # errorText = By.XPATH, '//h3'