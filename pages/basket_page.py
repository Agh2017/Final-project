from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_item_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NO_ITEM), "Basket isn't empty"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
