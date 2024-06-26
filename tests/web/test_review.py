import allure
import pytest
from sofrino_auto_test.pages.ui.review_page import steps_reviuw
from sofrino_auto_test.test_data.data import dynamic_review, static_review


@allure.tag('web')
@allure.epic('Отзыв UI')
@pytest.mark.web
@allure.step(f"Проверка отправки отзыва: генерируемые  данные {dynamic_review}")
@pytest.fixture
def test_review_dynamic_send():
    steps_reviuw.fild_review(dynamic_review)
    steps_reviuw.should_review()


@allure.tag('web')
@allure.epic('Отзыв UI')
@pytest.mark.web
@allure.step(f"Проверка отправки отзыва: статичные данные {static_review}")
@pytest.fixture
def test_review_static_send():
    steps_reviuw.fild_review(dynamic_review)
    steps_reviuw.should_review()
