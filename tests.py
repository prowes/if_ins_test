''' Just some tests to check the saucedemo website.
To run: pytest [--headed -s] tests.py'''
from playwright.sync_api import Page
from locators import LoginPage, InventoryScreen, Checkout, Cart, CheckoutOverview, SidebarMenu, CompletedView
from data import URL, USERS, USERS_PASS
import pytest

#  split this file into 3?
def test_customer_purchases_three_products(page: Page):  # also refactor with POM
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["STANDART_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()

    assert page.locator(InventoryScreen.all_inventory).is_visible(), 'The products list is not visible'
    page.locator(InventoryScreen.add_backpack_to_cart).click()
    page.locator(InventoryScreen.add_light_to_cart).click()
    page.locator(InventoryScreen.go_to_cart).click()

    assert page.locator(Cart.cart_list).is_visible(), "The list of items in the cart is not shown"
    page.locator(Cart.checkout).click()

    page.locator(Checkout.first_name).fill("Bob")
    page.locator(Checkout.second_name).fill("Smith")
    page.locator(Checkout.zip_code).fill("000000")
    page.locator(Checkout.continue_order).click()

    assert page.locator(CheckoutOverview.summary_info).is_visible()
    page.locator(CheckoutOverview.finish_order).click()

    assert page.locator(CompletedView.complete_screen_title).is_visible(), "The Thank you... title is not shown"
    assert page.locator(CompletedView.complete_screen_title).is_visible(), "The Thank you... text is not shown"
    page.locator(CompletedView.back_home).click()
    assert page.locator(InventoryScreen.all_inventory).is_visible(), 'The products list is not visible'

    page.locator(SidebarMenu.open_sidebar_menu).click()
    page.locator(SidebarMenu.logout).click()
    assert page.locator(LoginPage.login_form_container).is_visible(), "User did not get back to the login screen"


def test_user_sorting_cheap_to_expensive(page: Page):
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["STANDART_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()
    page.locator(InventoryScreen.sorting_options).select_option(InventoryScreen.low_high)

    all_product_prices_shown = page.locator(InventoryScreen.item_price).all_inner_texts()
    print(all_product_prices_shown)
    all_product_prices_digits = list(map(lambda x: float(x.strip('$')), all_product_prices_shown))
    assert all_product_prices_digits == sorted(all_product_prices_digits), "Items are not sorted from low to high"


def test_user_sorting_expensive_to_cheap(page: Page):
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["STANDART_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()

    page.locator(InventoryScreen.sorting_options).select_option(InventoryScreen.high_low)
    all_product_prices_shown = page.locator(InventoryScreen.item_price).all_inner_texts()
    print(all_product_prices_shown)
    all_product_prices_digits = list(map(lambda x: float(x.strip('$')), all_product_prices_shown))
    assert all_product_prices_digits == sorted(all_product_prices_digits, reverse=True), "Items are not sorted from high to low"


def test_user_sorting_a_to_z(page: Page):
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["STANDART_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()

    page.locator(InventoryScreen.sorting_options).select_option(InventoryScreen.sorting_a_z)
    all_product_names = page.locator(InventoryScreen.item_name).all_inner_texts()
    print(all_product_names)
    assert all_product_names == sorted(all_product_names), "Items are not sorted from A to Z"


def test_user_sorting_z_to_a(page: Page):
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["STANDART_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()

    page.locator(InventoryScreen.sorting_options).select_option(InventoryScreen.sorting_z_a)
    all_product_names = page.locator(InventoryScreen.item_name).all_inner_texts()
    print(all_product_names)
    assert all_product_names == sorted(all_product_names, reverse=True), "Items are not sorted from Z to A"


def test_user_is_locked_from_the_platform(page: Page):
    response = page.goto(URL)
    assert response.ok, 'The website does not reply with OK response, please check'
    page.locator(LoginPage.name_form).fill(USERS["LOCKED_USER_NAME"])
    page.locator(LoginPage.pass_form).fill(USERS_PASS)
    page.locator(LoginPage.login_button).click()
    assert page.locator(LoginPage.error_message).is_visible(), "Error message is not shown for the blocked user"
