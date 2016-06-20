Feature: Users

    Scenario: Register
      Given Visit the url "https://testing.alytics.ru/"
      When Click the link ".js-to-register"
      And Fill input "#name" with "some_name"
      And Fill input "#company" with "google"
      And Fill input "#site" with "google.com"
      And Fill input "#work" with "developer"
      And Fill input "#email" with "developer@developer.com"
      And Fill input "#phone" with "123456"
      And Fill input "#password1" with "qwerty"
      And Fill input "#password2" with "qwerty"
      And Fill input "#promo_code" with "TEST PROMO"
      And Click the button ".js-reg-submit"
      Then See the queue message
      And User should be present in the database:
          | username                 |
          | developer@developer.com  |

    Scenario: Login
        Given Visit the url "https://testing.alytics.ru/"
        When Fill login "#req1" with "test"
        When Fill password "#req2" with "1"
        And Click the button "[type=submit]"
        Then See the project "test" in list