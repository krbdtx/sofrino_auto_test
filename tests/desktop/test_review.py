import allure
import pytest
from pages.ui.review_page import stepsreviuw
from test_data.data import rev1, rev2


@allure.tag('web')
@allure.epic('Отзыв UI')
@pytest.mark.web_test
@allure.step(f"Проверка отправки отзыва: генерируемые  данные {rev1}")
def test_review_dynamic_send():

    stepsreviuw.fild_review(rev1)
    stepsreviuw.should_review()


@allure.tag('web')
@allure.epic('Отзыв UI')
@pytest.mark.web_test
@allure.step(f"Проверка отправки отзыва: статичные данные {rev2}")
def test_review_static_send():

    stepsreviuw.fild_review(rev1)
    stepsreviuw.should_review()
