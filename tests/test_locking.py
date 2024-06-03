''' A test to check the saucedemo website and the lockes user flow.
To run: pytest [--headed] test_purchases.py'''
from data import USERS, USERS_PASS
from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_user_is_locked_from_the_platform(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.log_into_website(USERS['LOCKED_USER_NAME'], USERS_PASS)

    assert login_page.error_message.is_visible(), 'Error message is not shown for the blocked user'
