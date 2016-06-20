from lettuce import before, after, world
from selenium import webdriver


@before.all
def set_browser():
    world.browser = webdriver.Firefox()


# @after.all
# def close_browser():
#     world.browser.quit()