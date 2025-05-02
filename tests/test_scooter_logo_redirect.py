import allure

from data import CREATE_ORDER_URL, MAIN_PAGE_URL
from pages.scooter_logo_redirect_page import ScooterLogoRedirectPage


class TestScooterLogoRedirectPage:

    @allure.title('Тесты на проверку перехода на главную по логотипу "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        scooter_logo = ScooterLogoRedirectPage(driver)
        scooter_logo.go_to_url(CREATE_ORDER_URL)
        scooter_logo.click_to_logo()
        assert scooter_logo.get_current_url() == MAIN_PAGE_URL