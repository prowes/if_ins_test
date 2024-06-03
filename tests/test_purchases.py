''' Just some tests to check the saucedemo website.
To run: pytest [--headed -s] tests.py'''
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_screen import InventoryScreen
from pages.cart import CartScreen
from pages.checkout import CheckoutScreen
from pages.checkoutoverview import CheckoutOverviewScreen
from pages.completed import CompletedViewScreen
from data import USERS, USERS_PASS


def test_customer_purchases_three_products(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.username.fill(USERS['STANDART_USER_NAME'])
    login_page.password.fill(USERS_PASS)
    login_page.login_button.click()

    inventory_screen = InventoryScreen(page)
    assert inventory_screen.all_inventory.is_visible, 'The products list is not visible'
    inventory_screen.add_backpack_to_cart.click()
    inventory_screen.add_light_to_cart.click()
    inventory_screen.go_to_cart.click()

    cart_screen = CartScreen(page)
    assert cart_screen.cart_list.is_visible(), 'The list of items in the cart is not shown'
    cart_screen.checkout.click()

    checkout_screen = CheckoutScreen(page)
    checkout_screen.first_name.fill('Bob')
    checkout_screen.second_name.fill('Smith')
    checkout_screen.zip_code.fill('000000')
    checkout_screen.continue_order.click()

    checkout_overview = CheckoutOverviewScreen(page)
    assert checkout_overview.summary_info.is_visible(), 'The summary info is not visible'
    checkout_overview.finish_order.click()

    completed_view = CompletedViewScreen(page)
    assert completed_view.complete_screen_title.is_visible(), 'The Thank you... title is not shown'
    assert completed_view.complete_screen_text.is_visible(), 'The Thank you... text is not shown'
    completed_view.back_home.click()
    assert inventory_screen.all_inventory.is_visible, 'The products list is not visible, most likely user did not get back'

    inventory_screen.open_sidebar_menu.click()
    inventory_screen.logout.click()
    assert login_page.login_form_container.is_visible(), 'User did not get back to the login screen'
