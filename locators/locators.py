from selenium.webdriver.common.by import By


class Locators:
    userName = (By.ID, 'user-name')
    password = (By.ID, 'password')
    submitButton = (By.ID, 'login-button')
    swagLabsText = By.XPATH, '//div[@class ="app_logo"]'
    burgerMenu = By.ID, 'react-burger-menu-btn'
    logoutButton = By.ID, 'logout_sidebar_link'
    userName1 = (By.ID, 'user-name')
    password1 = (By.ID, 'password')
    TextMessage = By.XPATH, '//h3'
    userName2 = (By.ID, 'user-name')
    password2 = (By.ID, 'password')

