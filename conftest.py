import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data import MAIN_PAGE_URL


@pytest.fixture
def driver():

    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(MAIN_PAGE_URL)
    yield firefox
    firefox.quit()