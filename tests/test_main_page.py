import pytest
import allure

from data import ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_1),
            (1, ANSWER_2),
            (2, ANSWER_3),
            (3, ANSWER_4),
            (4, ANSWER_5),
            (5, ANSWER_6),
            (6, ANSWER_7),
            (7, ANSWER_8),
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        allure.dynamic.title(f'Тесты на проверку вопроса {num+1}')
        main_page = MainPage(driver)
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == result

