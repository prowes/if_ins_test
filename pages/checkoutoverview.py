from locators import CheckoutOverviewLocators

class CheckoutOverviewScreen:
    """
    A class to represent the checkout overview page and its elements.
    """

    def __init__(self, page):
        self.page = page
        self.summary_info = page.locator(CheckoutOverviewLocators.summary_info)
        self.cancel_order = page.locator(CheckoutOverviewLocators.cancel_order)
        self.finish_order = page.locator(CheckoutOverviewLocators.finish_order)
