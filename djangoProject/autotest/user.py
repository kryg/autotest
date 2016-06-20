# -*- coding: utf-8; show-trailing-whitespace: t -*-

from lettuce import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User


@before.each_scenario
def reset_cookie(scenario):
    User.objects.filter(username='developer@developer.com').delete()
    world.browser.delete_all_cookies()

@step('See the queue message')
def queue_message(step):
    element = WebDriverWait(world.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "queue-text"))
    )
    assert element.text == u'Ваш номер в очереди:'
