import allure

from locators.scooter_logo_redirect_locators import ScooterLogoRedirectLocators
from pages.base_page import BasePage


class ScooterLogoRedirectPage(BasePage):

    @allure.step('Открываем страницу {url}')
    def go_to_url(self, url):
        return self.driver.get(url)

    @allure.step('Кликаем на логотип "Самоката"')
    def click_to_logo(self):
        self.click_to_element(ScooterLogoRedirectLocators.SCOOTER_LOGO)
