''' Just some tests to check the saucedemo website.
To run: pytest [--headed -s] tests.py'''
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_screen import InventoryScreen
from data import USERS, USERS_PASS


def test_user_sorting_cheap_to_expensive(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.log_into_website(USERS['STANDART_USER_NAME'], USERS_PASS)

    inventory_screen = InventoryScreen(page)
    assert inventory_screen.all_inventory.is_visible(), 'The products list is not visible'
    inventory_screen.sorting_dropdown.select_option(inventory_screen.low_high)
    assert inventory_screen.test_price_sorting_is_working(False), 'Items are not sorted from low to high'


def test_user_sorting_expensive_to_cheap(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.log_into_website(USERS['STANDART_USER_NAME'], USERS_PASS)

    inventory_screen = InventoryScreen(page)
    assert inventory_screen.all_inventory.is_visible(), 'The products list is not visible'
    inventory_screen.sorting_dropdown.select_option(inventory_screen.high_low)
    assert inventory_screen.test_price_sorting_is_working(True), 'Items are not sorted from low to high'


def test_user_sorting_a_to_z(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.log_into_website(USERS['STANDART_USER_NAME'], USERS_PASS)

    inventory_screen = InventoryScreen(page)
    assert inventory_screen.all_inventory.is_visible(), 'The products list is not visible'
    inventory_screen.sorting_dropdown.select_option(inventory_screen.sorting_a_z)
    assert inventory_screen.test_name_sorting_is_working(False), 'Names are not sorted from A to Z'


def test_user_sorting_z_to_a(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.log_into_website(USERS['STANDART_USER_NAME'], USERS_PASS)

    inventory_screen = InventoryScreen(page)
    assert inventory_screen.all_inventory.is_visible(), 'The products list is not visible'
    inventory_screen.sorting_dropdown.select_option(inventory_screen.sorting_z_a)
    assert inventory_screen.test_name_sorting_is_working(True), 'Names are not sorted from Z to A'
