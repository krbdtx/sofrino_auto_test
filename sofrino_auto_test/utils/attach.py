import json
import allure
from allure_commons.types import AttachmentType
from requests import Response
import logging


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def request_url_and_body(response):
    allure.attach(
        body=response.request.url,
        name="Request URL",
        attachment_type=AttachmentType.TEXT,
        extension="txt")

    allure.attach(
        body=response.request.body,
        name="Request payload",
        attachment_type=AttachmentType.TEXT,
        extension="txt")


def response_json_and_cookies(response):
    allure.attach(
        body=json.dumps(response.json(),
                        indent=4,
                        ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json")

    allure.attach(
        body=str(response.cookies),
        name="Cookies",
        attachment_type=AttachmentType.TEXT,
        extension="txt")


def logging_response(response):
    logging.info(response.request.url)
    logging.info(response.status_code)
    logging.info(response.text)
