# Created by kryg at 6/20/16
Feature: CreateProject

#    Scenario: Authorization
#        Given Visit the url "authorization"
#        When Fill "username" with "vskr@alytics-team.com"
#        When Fill "password" with "314159265"
#        And Click "login button"
#        Then Wait appearance "class success"
#        Then See the queue "success_message" in "test_message" and "username"
#        When Fill "username" with "world.test"
#        Then See the project "test" in list

  Scenario: Create
        Given Visit the url "createProject"
        When Fill "username" with "vskr@alytics-team.com"
        When Fill "password" with "314159265"
        And Click "login button"
        And "add project button" to be clickable
        And Click "add project button"
        And Fill "name project" with "ABC"
        And Fill "name site" with "it_project.com"
        And Click "button submit form"
        And Wait appearance "login YD in Alytics"
        And Fill "login YD in Alytics" with "VK.autotest"
        And Click "button submit form"
        And Switch to new window opened
        And Wait appearance "login YD in YD"
        And Fill "login YD in YD" with "VK.autotest"
        And Fill "passwd YD in YD" with "314159265"
        And Click "button submit form YD"
        And Switch to new window opened
        And Wait disappearance "animation loading"
        And Click "radio button all company"
        And Click "button submit form"
        And Wait disappearance "animation loading"
        And Click "button submit form"
        And Switch to new window opened
        And Fill "email GE" with "vskr@alytics-team.com"
        And Click "button next"
        And Wait appearance "passwd GE"
        And Fill "passwd GE" with "kryg314159265"
        And Click "button signIn GE"
        And Switch to new window opened
        And "button submit approve access" to be clickable
        And Click "button submit approve access"
        And Switch to new window opened
        And Wait disappearance "animation loading"
        And Click "radio all data"
        And Click "button submit form"
        And Wait appearance "selector add goals"
        And Click "button submit form"
        And Wait appearance "selector add utm"
        And Click "button submit form"
        And Wait disappearance "animation loading"
        And Click "button to see the project"
        And Wait disappearance "animation loading"

#      And Wait appearance ".logo"
#    ________________________
#      And Click the button ".logo"
#      And Wait disappearance ".progress-bar"
#  ________________
#      And Wait appearance ".gradeA"
#      Then See the project "ABC" in list