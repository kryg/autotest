Feature: CreateProjects

    Scenario: Create
      Given Visit the url "https://testing.alytics.ru/"
      When Fill login "#req1" with "test"
      And Fill password "#req2" with "1"
      And Click the button "[type=submit]"
      And Click the button ".add-project-button"
      And Fill project name "#project-input-0" with "it_project"
      And Fill project name "#project-input-1" with "it_project.com"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Fill YD login "#project-input-0" with "yd-test"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the radiobutton "[name='project[yandex_client]']:first-of-type"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the radiobutton ".all-campaigns"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click checkbox ".js-profile-value:first-of-type"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Wait appearance ".submit-form:not([disabled])"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Wait appearance "[name=utm_medium]"

#      And Click the button ".submit-form"
#      And Wait disappearance ".progress-bar"
#      And Click the button ".addProject"
#      Then See the project "test" in list





