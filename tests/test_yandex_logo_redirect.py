import allure

from data import YANDEX_URL
from pages.yandex_logo_redirect_page import YandexLogoRedirectPage



class TestYandexLogoRedirectPage:

    @allure.title('Тесты на проверку перехода на Яндкес-Дзен по логотипу "Yandex"')
    def test_yandex_logo_redirect(self, driver):
        yandex_logo = YandexLogoRedirectPage(driver)
        yandex_logo.click_to_logo()
        yandex_logo.switch_to_next_tab()
        login_button = yandex_logo.get_yandex_login_button()
        current_url = yandex_logo.get_current_url()
        assert current_url == YANDEX_URL and login_button.is_displayed()