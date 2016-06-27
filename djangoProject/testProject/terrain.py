from lettuce import before, after, world
from selenium import webdriver
from mapping import site_mapping

@before.all
def set_browser():
    world.browser = webdriver.Firefox()
    world.mapping = site_mapping

# @after.all
# def close_browser():
#     world.browser.quit()