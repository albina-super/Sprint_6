from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}" and contains(@class, "accordion__button")]'
    ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_FOR_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]'
