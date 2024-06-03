from data import URL
from locators import LoginPageLocators

class LoginPage:
    '''
    A class to represent the login page and its elements.
    '''

    def __init__(self, page):
        self.page = page
        self.login_form_container = page.locator(LoginPageLocators.login_form_container)
        self.username = page.locator(LoginPageLocators.name_form)
        self.password = page.locator(LoginPageLocators.pass_form)
        self.login_button = page.locator(LoginPageLocators.login_button)
        self.error_message = page.locator(LoginPageLocators.error_message)


    def load(self):
        response = self.page.goto(URL)
        assert response.ok, 'The website does not reply with OK response, please check'


    def log_into_website(self, name, password):
        self.username.fill(name)
        self.password.fill(password)
        self.login_button.click()
