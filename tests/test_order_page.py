
import pytest
import allure

from data import DATA_FOR_FIRST_ORDER, DATA_FOR_SECOND_ORDER
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
        (OrderPageLocators.CREATE_ORDER_UP, DATA_FOR_FIRST_ORDER),
        (OrderPageLocators.CREATE_ORDER_DOWN, DATA_FOR_SECOND_ORDER),
        ]
    )
    def test_order_page(self, driver, locator, order_data):
        allure.dynamic.title('Тестируем создание заказа')
        order_page = OrderPage(driver)
        order_page.scroll_to_element(locator)
        order_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert 'Заказ оформлен' in order_page.check_alert_of_created_order()
