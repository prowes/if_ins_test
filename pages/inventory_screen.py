from locators import InventoryScreenLocators

class InventoryScreen:
    '''
    A class to represent the inventory page and its elements.
    '''

    def __init__(self, page):
        self.page = page
        self.all_inventory = page.locator(InventoryScreenLocators.all_inventory)

        self.add_backpack_to_cart = page.locator(InventoryScreenLocators.add_backpack_to_cart)
        self.add_light_to_cart = page.locator(InventoryScreenLocators.add_light_to_cart)
        self.go_to_cart = page.locator(InventoryScreenLocators.go_to_cart)
        self.open_sidebar_menu = page.locator(InventoryScreenLocators.open_sidebar_menu)
        self.logout = page.locator(InventoryScreenLocators.logout)

        self.sorting_dropdown = page.locator(InventoryScreenLocators.sorting_options)
        self.sorting_a_z = 'az'
        self.sorting_z_a = 'za'
        self.low_high = 'lohi'
        self.high_low = 'hilo'

        self.item_prices = page.locator(InventoryScreenLocators.item_price)
        self.item_name = page.locator(InventoryScreenLocators.item_name)


    def test_price_sorting_is_working(self, decreasing):
        all_prices_shown = self.item_prices.all_inner_texts()
        print(all_prices_shown)
        all_prices_digits = list(map(lambda x: float(x.strip('$')), all_prices_shown))
        return all_prices_digits == sorted(all_prices_digits, reverse = decreasing)


    def test_name_sorting_is_working(self, decreasing):
        all_product_names = self.item_name.all_inner_texts()
        print(all_product_names)
        return all_product_names == sorted(all_product_names, reverse = decreasing)
