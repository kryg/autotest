# Created by kryg at 6/17/16
# -*- coding: utf-8; show-trailing-whitespace: t -*-

Feature: Authorization in testing.alytics.ru

  Scenario: Authorization
        Given Visit the url "authorization"
        When Fill "username" with "vskr@alytics-team.com"
        When Fill "password" with "314159265"
        And Click "login button"
        Then Wait appearance "class success"
#        Then See the queue "success_message" in "test_message" and "username"
#        When Fill "username" with "world.test"
#        Then See the project "test" in list