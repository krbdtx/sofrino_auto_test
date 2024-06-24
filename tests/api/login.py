import requests


LOGIN = "фыв@фыв.com"
PASSWORD = "123123"
API_URL = "https://sofrino.ru/login"
WEB_URL = "https://sofrino.ru/users/lk"



result = requests.post(
            url=API_URL,
            data={"action": "login", "email": LOGIN, "password": PASSWORD})
        #allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        #allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
print(result.status_code)
print(result.text)
print(result.cookies.get(""))
print(requests.Session.get(url=WEB_URL, cookies="UserToken"))

