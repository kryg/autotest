# -*- coding: utf-8; show-trailing-whitespace: t -*-


from lettuce import step, world
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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


@step('See the queue message')
def queue_message(step):
    element = WebDriverWait(world.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "queue-text"))
    )
    assert element.text == u'Ваш номер в очереди:'


@step('should be present in the database')
def queue_message(step):
    element = WebDriverWait(world.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "queue-text"))
    )
    assert element.text == u'Ваш номер в очереди:'


@step('Wait disappearance "(.*)"')
def wait_for(step, selector):
    WebDriverWait(world.browser, 200).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


@step('Wait appearance "(.*)"')
def wait_for(step, selector):
    WebDriverWait(world.browser, 200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


@step('Switch to new window opened')
def wait_for(step):
    for handle in world.browser.window_handles:
        world.browser.switch_to_window(handle)




@step('"(.*)" to be clickable')
def wait_for(step,selector):
    WebDriverWait(world.browser, 100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )


@step(r'See the project "(.*)" in list')
def have_project(step, project_name):
    world.browser.find_element_by_name('project_name')
# def have_project(step, project_name):
#     project_href = world.browser.find_element_by_css_selector('.chzn-results').find_element_by_tag_name('li')
#     assert project_href.text == project_name

