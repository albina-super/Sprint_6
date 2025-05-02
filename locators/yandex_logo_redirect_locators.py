from selenium.webdriver.common.by import By


class YandexLogoRedirectLocators:
    YANDEX_LOGO = By.XPATH, '//*[contains(@class, "Header_LogoYandex")]'
    YANDEX_LOGIN_BUTTON = By.XPATH, '//button[@data-testid="login-button" and span[text()="Войти"]]'