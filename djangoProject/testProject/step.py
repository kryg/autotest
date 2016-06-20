# -*- coding: utf-8; show-trailing-whitespace: t -*-


from lettuce import step, world
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step(r'Visit the url "(.*)"')
def open_url(step, url):
    world.browser.get(url)


@step(r'Fill "(.*)" with "(.*)"')
def fill_element_with_text(step, selector, text):
    el = world.browser.find_element_by_css_selector(selector)
    el.send_keys(text)


@step(r'Click "(.*)"')
def click_element(step, selector):
    button = world.browser.find_element_by_css_selector(selector)
    button.click()


@step(r'Click the button "(.*)"')
def click_element(step, selector):
    button = world.browser.find_element_by_css_selector(selector)
    button.click()


# @step('See the queue message')
# def queue_message(step):
#     element = WebDriverWait(world.browser, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "queue-text"))
#     )
#     assert element.text == u'Ваш номер в очереди:'