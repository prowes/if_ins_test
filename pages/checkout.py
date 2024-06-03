from locators import CheckoutLocators

class CheckoutScreen:
    """
    A class to represent the checkout page and its elements.
    """

    def __init__(self, page):
        self.page = page
        self.first_name = page.locator(CheckoutLocators.first_name)
        self.second_name = page.locator(CheckoutLocators.second_name)
        self.zip_code = page.locator(CheckoutLocators.zip_code)
        self.cancel_order = page.locator(CheckoutLocators.cancel_order)
        self.continue_order = page.locator(CheckoutLocators.continue_order)
