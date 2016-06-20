# -*- coding: utf-8; show-trailing-whitespace: t -*-

from lettuce import *
from selenium import webdriver


@before.all
def set_browser():
    world.browser = webdriver.Firefox()

@after.all
def close_browser():
    world.browser.quit()

@after.each_scenario
def save_screenshot_on_error(scenario):
    if scenario.failed:
        scenario_name = '{0}-{1}'.format(scenario.feature.name, scenario.name)
        print 'Last URL: {0}'.format(world.browser.current_url)
        world.browser.get_screenshot_as_file('{0}.png'.format(scenario_name))
        with open('{0}.html'.format(scenario_name), 'w') as f:
            f.write(world.browser.page_source.encode('utf-8'))