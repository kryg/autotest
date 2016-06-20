# Created by kryg at 6/17/16
Feature: Authorization in testing.alytics.ru

  Scenario: Authorization
        Given Visit the url "https://testing.alytics.ru/"
        When Fill "#req1" with "vskr@alytics-team.com"
        When Fill "#req2" with "314159265"
        And Click "[type=submit]"
#        Then See the project "test" in list