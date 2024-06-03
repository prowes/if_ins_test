from locators import CartLocators

class CartScreen:
    """
    A class to represent the cart page and its elements.
    """

    def __init__(self, page):
        self.page = page
        self.cart_list = page.locator(CartLocators.cart_list)
        self.continue_shopping = page.locator(CartLocators.continue_shopping)
        self.checkout = page.locator(CartLocators.checkout)
