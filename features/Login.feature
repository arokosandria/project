Feature: Login
  Scenario: Log success
   Given user is on saucedemo
   When Fill login and password
   Then Login success
 Scenario: Log not success with not register user
   Given user is on saucedemo next
   When Fill login and password bad
   Then Login not success
  Scenario: Log not success with bad password
   Given user is on saucedemo next iteral
   When Fill password bad
   Then Login not success with bad password