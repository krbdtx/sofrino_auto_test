import allure
from model.pages_top import top_lvl
from data.small_bd import Review
from faker import Faker
fake = Faker()

rev1 = Review(name=fake.name(), phone=fake.phone_number(),
              reviews=fake.text(100))
rev2 = Review(name='Робот', phone='9876543210',
              reviews='Здравствуйте Уважаемые коллеги, это тестовый робот для тренировки, ваш ресурс прекрасно для этого подходит, уже вышел!!!')


@allure.step(f"Проверка отправки отзыва {rev1}")
def test_review_send_01():

    top_lvl.fild_review(rev1)
    top_lvl.should_review()


@allure.step(f"Проверка отправки отзыва {rev2}")
def test_review_send_02():

    top_lvl.fild_review(rev2)
    top_lvl.should_review()
