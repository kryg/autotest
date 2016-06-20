# -*- coding: utf-8; show-trailing-whitespace: t -*-

from lettuce import *
from lettuce.django import django_url
from lettuce.django.steps.models import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@step(r'Visit the url "(.*)"')
def access_url(step, url):
    world.browser.get(url)

@step(r'See the project "(.*)" in list')
def have_project(step, project_name):
    project_href = world.browser.find_element_by_css_selector('.projects-list').find_element_by_tag_name('td').\
        find_element_by_tag_name('a')
    assert project_href.text == project_name

@step('Click(.+)? "(.*)"')
def click_element(step, stub, selector):
    button = world.browser.find_element_by_css_selector(selector)
    button.click()

@step('Fill(.+)? "(.*)" with "(.*)"')
def fill_in_element(step, stub, selector, text):
    el = world.browser.find_element_by_css_selector(selector)
    el.send_keys(text)

@step('Wait for text "(.*)" in "(.*)"')
def wait_for(step, text, selector):
    element = WebDriverWait(world.browser, 200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    assert element.text == text

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
