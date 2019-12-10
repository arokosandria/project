Feature: Login
  Scenario: Correct Log
    Given user is on saucedemo
    When Fill login and password
    Then Login success

  Scenario Outline: Bad Log
   Given user is on saucedemo
   When Fill "<login>" and "<password>"
   Then View "<messeage>"
    Examples: Login

    |login            |password      |messeage                                                                 |
    |user-name        | abc           |Epic sadface: Username and password do not match any user in this service   |
    |abc              | abc           |Epic sadface: Username and password do not match any user in this service   |
    |locked_out_user  | secret_sauce  |Epic sadface: Sorry, this user has been locked out. |

  Scenario: Correct Log and Logout
    Given user is on saucedemo
    When Fill login and password
    Then Login success and logout