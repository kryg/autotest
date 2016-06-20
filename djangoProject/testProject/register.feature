# Created by kryg at 6/17/16
Feature: Register in testing.alytics.ru

  Scenario: Register
    Given Visit the url "https://testing.alytics.ru/"
      When Click ".js-to-register"
      And Fill "#name" with "autotest111"
      And Fill "#company" with "KVautotest"
      And Fill "#site" with "autotest.com"
      And Fill "#work" with "developer"
      And Fill "#email" with "autot1est1@develope11r.com"
      And Fill "#phone" with "123456"
      And Fill "#password1" with "qwerty"
      And Fill "#password2" with "qwerty"
      And Fill "#promo_code" with "TEST PROMO"
      And Click the button ".js-reg-submit"
      Then See the queue message
      And User should be present in the database:
          | autotest111                |
          | autot1est1@develope11r.com  |