from locators import CompletedViewLocators

class CompletedViewScreen:
    """
    A class to represent the completed page and its elements.
    """

    def __init__(self, page):
        self.page = page
        self.complete_screen_title = page.locator(CompletedViewLocators.complete_screen_title)
        self.complete_screen_text = page.locator(CompletedViewLocators.complete_screen_text)
        self.back_home = page.locator(CompletedViewLocators.back_home)
