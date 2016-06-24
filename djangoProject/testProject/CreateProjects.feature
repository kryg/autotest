# Created by kryg at 6/20/16
Feature: CreateProjects

  Scenario: Create
    Given Visit the url "https://testing.alytics.ru/"
      When Fill "#req1" with "vskr@alytics-team.com"
      When Fill "#req2" with "314159265"
      And Click "[type=submit]"
      And ".add-project-button" to be clickable
      And Click the button ".add-project-button"
      And Fill "#project-input-0" with "ABC"
      And Fill "#project-input-1" with "it_project.com"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Fill "#project-input-0" with "VK.autotest"
      And Click the button ".submit-form"
      And Switch to new window opened
      And Wait appearance "#login"
      And Fill "#login" with "VK.autotest"
      And Fill "#passwd" with "314159265"
      And Click ".domik-submit-button"
      And Switch to new window opened
      And Wait disappearance ".progress-bar"
      And Click ".all-campaigns"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the button ".submit-form"
      And Switch to new window opened
      And Fill "#Email" with "vskr@alytics-team.com"
      And Click "#next"
      And Wait appearance "#Passwd"
      And Fill "#Passwd" with "kryg314159265"
      And Click "#signIn"
      And Switch to new window opened
      And "#submit_approve_access" to be clickable
      And Click "#submit_approve_access"
      And Switch to new window opened
      And Wait disappearance ".progress-bar"
      And Click ".js-profile-value:first-of-type"
      And Click the button ".submit-form"
#      And Wait disappearance ".progress-bar"
      And Wait appearance ".goal-name-placeholder"
#    _______________
#      And ".submit-form" to be clickable
#    в этом месте похоже слишком рано кликает на кнопку, в то время каак она не рбочая.
#      And Wait appearance ".submit-form:not([disabled])"
      And Click the button ".submit-form"
#      And Wait disappearance ".progress-bar"
      And Wait appearance "[name=utm_medium]"
      And Click the button ".submit-form"
      And Wait disappearance ".progress-bar"
      And Click the button ".addProject"
      And Wait disappearance ".progress-bar"






#      And Wait appearance ".logo"
#    ________________________
#      And Click the button ".logo"
#      And Wait disappearance ".progress-bar"
#  ________________
#      And Wait appearance ".gradeA"
#      Then See the project "ABC" in list