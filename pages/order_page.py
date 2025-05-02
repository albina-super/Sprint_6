import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Создаем ордер')
    def set_order(self, data):
        self.add_text_to_element(OrderPageLocators.INPUT_NAME, data['name'])
        self.add_text_to_element(OrderPageLocators.INPUT_LAST_NAME, data['last_name'])
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS, data['address'])
        self.click_to_element(OrderPageLocators.STATION_METRO_BUTTON)
        self.click_to_element(OrderPageLocators.METRO_INPUT_VALUE)
        self.add_text_to_element(OrderPageLocators.INPUT_NUMBER_PHONE, data['phone'])
        self.click_to_element(OrderPageLocators.NEXT_STEP_BUTTON)
        self.click_to_element(OrderPageLocators.DATE_OF_RENTAL_INPUT)
        self.click_to_element(OrderPageLocators.DATE_OF_RENTAL_IN_CALENDAR)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECTOR)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECTOR_VALUE)
        self.click_to_element(OrderPageLocators.COLOR_OF_SCOOTER_CHECKBOX)
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER_INPUT, data['comment'])
        self.click_to_element(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)


    @allure.step('Чекаем алерт после успешного создания ордера')
    def check_alert_of_created_order(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_CREATED_ORDER_ALERT)


