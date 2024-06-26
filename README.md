### Здравствуйте уважаемые посетители этого repo, тут расположен маленький проект автотестов ресурса sofrino.ru

> <a target="_blank" href="https://sofrino.ru/">sofrino.ru</a>

<details>
  <summary> #### Этот проект, дипломная работа по курсу QA.GURU | Python | Автоматизация тестирования 12 поток</summary>
В этом проект представлены демонстрационные тесты для практики и обучения на курсе.</summary>
</details>

#### Используемый стэк:

<div align="center">
    <img title="Pytest" width="50" src="resources/img/pytest-original-wordmark.svg">
    <img title="Selene" width="50" src="resources/img/selene.png">
    <img title="Jenkins" width="50" height="50" src="resources/img/Jenkins.png">
    <img title="Selenoid" width="50" src="resources/img/Selenoid.png">
    <img title="Allure" width="50" src="resources/img/Allure_Report.png">
    <img title="Allure" width="50" src="resources/img/appium.png">
    <img title="Allure" width="50" src="resources/img/browserstack.png">
    <img title="Allure" width="50" src="resources/img/telegram.png">
</div>

#### Cписко UI-автотестов в web:

- [x] [Страница поиск товара](tests/web/test_find_product.py) (позитив негатив)
-
    * Поиск существуюущего товара.(Ожидаем Успех)
-
    * Поиск не существуюущего товара. (Ожидаем Ошибку)
- [x] [Страница написать отзыв](tests/web/test_review.py) (позитив)
-
    * Отправка Отзыва со статичным текстом. (Ожидаем Успех)
-
    * Отправка Отзыва с динамическим текстом. (Ожидаем Успех)
- [x] [Страница Вход пользователя](tests/web/test_user_login.py) (позитив негатив)
-
    * Вход актуального пользователя. (Ожидаем Успех)
-
    * Вход не зарегистрированного пользователя статичные данные. (Ожидаем Ошибку)
-
    * Вход не зарегистрированного пользователя динамичные данные. (Ожидаем Ошибку)
- [x] [Страница Регистрация пользователя](tests/web/test_register_user.py) (позитив негатив)
-
    * Регистраиця сгенерированного пользователя. (Ожидаем Успех)
-
    * Регистраиця пользователя с не коректным e-mail. (Ожидаем Ошибку)
-
    * Регистраиця сгенерированного пользователя с пустым паролем. (Ожидаем Ошибку)

#### Cписко API-автотестов:

- [x] [Вход пользователя](tests/api/test_login.py) (позитив негатив)
-
    * Вход актуального пользователя. (Ожидаем Успех)
-
    * Вход актуального пользователя с не коректным паролем. (Ожидаем Ошибку)
- [x] [Получение корзины](tests/api/test_get_api.py) (позитив)
-
    * Получение корзины. (Ожидаем Успех)
- [x] [Получение формы отзыва](tests/api/test_get_api.py) (позитив)
-
    * Получение формы отзыва. (Ожидаем Успех)

#### Для локального автоматического запуска автотестов, запустить от администратора [starter.ps1](starter.ps1)

##### В cli PowerShell Выберете желаемые тесты введя цифру:

- [x] "1. Web"
- [x] "2. API"

<h3> Для локально ручного запуска автотестов:</h3>
<p><b>Запуск всех тестов</b></p>
<pre>
    pytest
</pre>
<p><b>Запуск web тестов</b></p>
<pre>
    pytest tests/web
</pre>
<p><b>Запуск API тестов</b></p>
<pre>
    pytest tests/api
</pre>

#### Для запуска автотестов в Jenkins

- [x] 
    1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C12-jonickc-diplom-TestOps-unit22/">
       проект</a>
- [x] 
    2. Выбрать пункт Собрать
- [x] 
    2. Дождаться оповещения в Tелеграм [канал](https://t.me/+D-lMxBsV3vFhOWUy)
- [x] 
    3. Подробный отчет запуска смотреть в
       отчёте [Allure](https://jenkins.autotests.cloud/job/C12-jonickc-diplom-TestOps-unit22/allure/)

#### Пример визуальных отчетов:

- [x] Оповещение в Телеграм

<div align="center">
    <img width="500" src="resources/img/teleg_report.PNG">
</div>

- [x] Общий отчет

![allure_rep_all_01.PNG](resources/img/allure_rep_all_01.PNG)

- [x] отчет кейса с ошибкой

![allure_rep_fail_01.PNG](resources/img/allure_rep_fail_01.PNG)

- [x] отчет успешного кейса

![allure_rep_good_01.PNG](resources/img/allure_rep_good_01.PNG)

- [x] Отчет в Allure TestOps

![allureTestOps.PNG](resources/img/allureTestOps.PNG)

- [x] Пример ручных тест-кейсов в Allure TestOps

![allureTestOps_case.PNG](resources/img/allureTestOps_case.PNG)

- [x] Пример интеграции с Jira

![jira.PNG](resources/img/jira.PNG)

- [x] Видео пример успешного кейса регистрации пользователя

![4295e6c98140b5964a79f97b49727288.gif](resources/img/4295e6c98140b5964a79f97b49727288.gif)
