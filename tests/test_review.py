import allure
from pages.steps import steps_on_pages
from test_data.data import Review
from faker import Faker
fake = Faker()

rev1 = Review(name=fake.name(), phone=fake.phone_number(),
              reviews=fake.text(100))
rev2 = Review(name='Робот', phone='9876543210',
              reviews='Здравствуйте Уважаемые коллеги, это тестовый робот для тренировки, ваш ресурс прекрасно для этого подходит, уже вышел!!!')


@allure.step(f"Проверка отправки отзыва {rev1}")
def test_review_dynamic_send():

    steps_on_pages.fild_review(rev1)
    steps_on_pages.should_review()


@allure.step(f"Проверка отправки отзыва {rev2}")
def test_review_static_send():

    steps_on_pages.fild_review(rev2)
    steps_on_pages.should_review()
