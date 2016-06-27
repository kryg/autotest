# Created by kryg at 6/17/16
Feature: Register in testing.alytics.ru

  Scenario: Registration
    Given Visit the url "registration"
      When Click "registration button"
      And Fill "full_name" with "autotest1151111"
      And Fill "company" with "KVautotest"
      And Fill "site" with "autotest.com"
      And Fill "position" with "developer"
      And Fill "email" with "autot1est1@develope111511r.com"
      And Fill "phone" with "123456"
      And Fill "password" with "qwerty"
      And Fill "verify password" with "qwerty"
      And Fill "promo_code" with "TEST PROMO"
      And Click "create_user_button"
      Then Wait appearance "class success"
#      And User should be present in the database:
#          | autotest111                |
#          | autot1est1@develope11r.com  |
