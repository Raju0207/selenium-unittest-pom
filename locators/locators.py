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

    photo = '//input[@type ="file"]'
    name = By.ID, 'name'
    save_change_button = By.XPATH, '//button[text() ="Save changes"]'
    balance_change_button = By.XPATH, '//button[text() = "Change"]'
    currency = By.XPATH, '//section[@class="sc-hKinHC cRHiry"]/button[4]'
    save_button = By.XPATH, '//button[text() = "Save"]'
