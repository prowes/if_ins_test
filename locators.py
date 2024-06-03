class LoginPageLocators:
    login_form_container = 'id=login_button_container'
    name_form = 'id=user-name'
    pass_form = 'id=password'
    login_button = 'id=login-button'
    error_message = '.error-button'


class InventoryScreenLocators:
    all_inventory = '.inventory_container'
    add_backpack_to_cart = 'id=add-to-cart-sauce-labs-backpack'
    add_light_to_cart = 'id=add-to-cart-sauce-labs-bike-light'
    go_to_cart = 'id=shopping_cart_container'
    sorting_options = '.product_sort_container'
    item_name = '.inventory_item_name'
    item_price = '.inventory_item_price'
    open_sidebar_menu = 'id=react-burger-menu-btn'
    logout = 'id=logout_sidebar_link'


class CheckoutLocators:
    first_name = 'id=first-name'
    second_name = 'id=last-name'
    zip_code = 'id=postal-code'
    cancel_order = 'id=cancel'
    continue_order = 'id=continue'


class CartLocators:
    cart_list = '.cart_list'
    continue_shopping = 'id=continue-shopping'
    checkout = 'id=checkout'


class CheckoutOverviewLocators:
    summary_info = '.summary_info'
    cancel_order = 'id=cancel'
    finish_order = 'id=finish'


class CompletedViewLocators:
    complete_screen_title = '.complete-header'
    complete_screen_text = '.complete-text'
    back_home = 'id=back-to-products'
