Feature: Products
  Scenario: Products ascending albetically
    Given user is login
    When Click sort A-Z
    Then Sort A-Z and success
  Scenario: Products desc albetically
     Given user is login
     When Click sort Z-A
     Then Sort Z-A and success
  Scenario:Products ascending price
     Given user is login
     When Click sort low to hight
     Then Sort low to hight and success
  Scenario:Products desc price
     Given user is login
     When Click sort hight to low
     Then Sort hight to low and success