Feature: Error
  Scenario: Correct Log
    Given user is on saucedemo
    When Fill login and password problem_user
    When click product
    Then Check picture
