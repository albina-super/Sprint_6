import allure

from locators.yandex_logo_redirect_locators import YandexLogoRedirectLocators
from pages.base_page import BasePage


class YandexLogoRedirectPage(BasePage):

    @allure.step('Кликаем на иконку "Yandex"')
    def click_to_logo(self):
        self.click_to_element(YandexLogoRedirectLocators.YANDEX_LOGO)


    @allure.step('Переходим на следующую вкладку')
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])


    @allure.step('Проверяем кнопку логина на странице Яндекс-Дзен')
    def get_yandex_login_button(self):
        return self.find_element_with_wait(YandexLogoRedirectLocators.YANDEX_LOGIN_BUTTON)




