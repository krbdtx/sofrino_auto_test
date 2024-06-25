import allure

from sofrino_auto_test.test_data import ReviewData
from selene import browser, have, by


class Review:

    @allure.step('Открыть браузер')
    def open_browser(self, url) -> object:
        browser.open(url)
        return self

    @allure.step("заполнить поле имя формы отзыв")
    def fild_review_name_low(self, name):
        browser.element('[name="data[name]"]').type(name)
        return self

    @allure.step("заполнить поле номер телефона формы отзыв")
    def fild_review_phone_low(self, phone):
        browser.element('[name="data[phone]"]').type(phone)
        return self

    @allure.step("заполнить поле текст отзыва формы отзыв")
    def fild_review_low(self, reviews):
        browser.element('[name="data[review]"]').type(reviews)
        return self

    @allure.step("Нажать кнопку отправить отзыв")
    def submit_review_low(self):
        browser.element(by.text('Отправить')).click()
        return self

    @allure.step("Проверка отправки отзыва")
    def should_review_low(self):
        browser.element('.fs-16').should(have.exact_text('Ваш отзыв успешно отправлен.'))
        return self


class StepsReview:

    @allure.step('Заполнить и отправить отзыв')
    def fild_review(self, value: ReviewData):
        review.open_browser(url='/o-predpriyatii/otzyvy')
        review.fild_review_name_low(value.name)
        review.fild_review_phone_low(value.phone)
        review.fild_review_low(value.reviews)
        review.submit_review_low()
        return self

    @allure.step('Проверить запись об успешной отправке отзыва')
    def should_review(self):
        review.should_review_low()
        return self


stepsreviuw = StepsReview()
review = Review()
