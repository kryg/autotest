# Created by kryg at 6/17/16
Feature: Register in testing.alytics.ru

  Scenario: Register
    Given Visit the url "https://testing.alytics.ru/"
      When Click ".js-to-register"
      And Fill "#name" with "autotest"
      And Fill "#company" with "KVautotest"
      And Fill "#site" with "autotest.com"
      And Fill "#work" with "developer"
      And Fill "#email" with "autotest@developer.com"
      And Fill "#phone" with "123456"
      And Fill "#password1" with "qwerty"
      And Fill "#password2" with "qwerty"
      And Fill "#promo_code" with "TEST PROMO"
      And Click the button ".js-reg-submit"
      Then See the queue message