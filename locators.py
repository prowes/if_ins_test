class LoginPage:
    login_form_container = "id=login_button_container"
    name_form = "id=user-name"
    pass_form = "id=password"
    login_button = "id=login-button"
    error_message = ".error-button"

class InventoryScreen:
    all_inventory = ".inventory_container"
    add_backpack_to_cart = "id=add-to-cart-sauce-labs-backpack"
    add_light_to_cart = "id=add-to-cart-sauce-labs-bike-light"
    go_to_cart = "id=shopping_cart_container"
    sorting_options = ".product_sort_container"
    sorting_z_a = "za"
    sorting_a_z = "az"
    low_high = "lohi"
    high_low = "hilo"
    item_name = ".inventory_item_name"
    item_price = ".inventory_item_price"


class Checkout:
    first_name = 'id=first-name'
    second_name = 'id=last-name'
    zip_code = 'id=postal-code'
    cancel_order = 'id=cancel'
    continue_order = 'id=continue'


class Cart:
    cart_list = ".cart_list"
    continue_shopping = "id=continue-shopping"
    checkout = "id=checkout"


class CheckoutOverview:
    summary_info = '.summary_info'  # class
    cancel_order = 'id=cancel'
    finish_order = 'id=finish'


class SidebarMenu:
    open_sidebar_menu = "id=react-burger-menu-btn"
    logout = "id=logout_sidebar_link"


class CompletedView:
    complete_screen_title = ".complete-header"
    complete_screen_text = ".complete-text"
    back_home = "id=back-to-products"
