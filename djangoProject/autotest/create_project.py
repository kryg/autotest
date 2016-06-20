# -*- coding: utf-8; show-trailing-whitespace: t -*-

from lettuce import *


@before.each_scenario
def reset_cookie(scenario):
    world.browser.delete_all_cookies()
