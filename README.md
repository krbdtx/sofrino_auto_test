### Зравствуйте уважаемые посетители этого repo, тут расположен маленький проект автотестов ресурса sofrino.ru
> <a target="_blank" href="https://sofrino.ru/">sofrino.ru</a>


#### Используемый стэк:

<div align="center">
    <img title="Pytest" width="50" src="data/img/pytest-original-wordmark.svg">
    <img title="Selene" width="50" src="data/img/selene.png">
    <img title="Jenkins" width="50" height="50" src="data/img/Jenkins.png">
    <img title="Selenoid" width="50" src="data/img/Selenoid.png">
    <img title="Allure" width="50" src="data/img/Allure_Report.png">
</div>

#### Cписко UI-автотестов:

- [x] [поиск товара](tests/test_find_product) (позитив негатив) 
- [x] [написать отзыв](tests/test_review) (позитив негатив)
- [x] [Вход пользователя](tests/test_user_login) (позитив негатив)
- [x] [Регистрация пользователя](tests/test_register_user) (позитив негатив)

#### Для локального автоматического запуска автотестов, запустить от администратора [starter.ps1](starter.ps1)

#### Для локально ручного запуска автотестов:

- [x] 1. Подготовить тестовую машину
- [x] 2. Склонировать репозиторий
- [x] 3. Установить зависимости
- [x] 4. Запустить в корневой директори pytest

#### Для запуска автотестов в Jenkins

- [x] 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C12-jonickc-sofrno_mini_test-unit14/">проект</a>
- [x] 2. Выбрать пункт Собрать
- [x] 2. Дождаться оповещения в Tелеграм [канал](https://t.me/+D-lMxBsV3vFhOWUy)  
- [x] 3. Подробный отчет запуска смотреть в отчёте [Allure](https://jenkins.autotests.cloud/job/C12-jonickc-sofrno_mini_test-unit14/3/allure)

#### Пример визуальных отчетов:

- [x] Оповещение в Телеграм

<div align="center">
    <img width="500" src="data/img/teleg_report.PNG">
</div>

- [x] Общий отчет

<div align="center">
    <img width="500" src="data/img/allure_rep_all_01.PNG">
</div>

- [x] отчет кейса с ошибкой

<div align="center">
    <img width="500" src="data/img/allure_rep_fail_01.PNG">
</div>

- [x] отчет успешного кейса

<div align="center">
    <img width="500" src="data/img/allure_rep_good_01.PNG">
</div>

- [x] Видео пример успешного кейса регистрации пользователя 

<div align="center">
    <img width="500" src="data/img/4295e6c98140b5964a79f97b49727288.gif">
</div>