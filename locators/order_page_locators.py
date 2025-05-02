from selenium.webdriver.common.by import By


class OrderPageLocators:

    CREATE_ORDER_UP = By.XPATH, '//*[contains(@class, "Button_Button") and contains(text(), "Заказать")]'
    CREATE_ORDER_DOWN = By.XPATH, '//*[contains(@class, "Button_Middle") and contains(text(), "Заказать")]'


    INPUT_NAME = By.XPATH, '//input[@type="text" and contains(@placeholder, "* Имя")]'
    INPUT_LAST_NAME = By.XPATH, '//input[@type="text" and contains(@placeholder, "* Фамилия")]'
    INPUT_ADDRESS = By.XPATH, '//input[@type="text" and contains(@placeholder, "* Адрес: куда привезти заказ")]'
    INPUT_NUMBER_PHONE = By.XPATH, '//input[@type="text" and contains(@placeholder, "* Телефон: на него позвонит курьер")]'
    STATION_METRO_BUTTON = By.XPATH, '//*[contains(@class,"select-search__value")]'
    METRO_INPUT_VALUE = By.XPATH, '//button[.//div[text()="Черкизовская"]]'
    NEXT_STEP_BUTTON = By.XPATH, '//button[contains(@class, "Button") and text()="Далее"]'
    DATE_OF_RENTAL_INPUT = By.XPATH, '//input[contains(@class,"Input_Input") and contains(@placeholder, "* Когда привезти самокат")]'
    DATE_OF_RENTAL_IN_CALENDAR = By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="18"]'
    RENTAL_PERIOD_SELECTOR = By.XPATH, '//div[@class="Dropdown-root"]'
    RENTAL_PERIOD_SELECTOR_VALUE = By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'
    COLOR_OF_SCOOTER_CHECKBOX = By.ID, "grey" # grey or black color
    COMMENT_FOR_COURIER_INPUT = By.XPATH, '//input[contains(@class,"Input_Input") and contains(@placeholder, "Комментарий для курьера")]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'
    CONFIRM_ORDER_BUTTON = By.XPATH, '//button[contains(@class,"Button") and text()="Да"]'
    SUCCESS_CREATED_ORDER_ALERT = By.XPATH, '//div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]'