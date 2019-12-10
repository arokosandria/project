Feature: Buy
  Scenario: Add product to the basket
    Given user is login
    When Click add to cart
    Then User see product in basket
  Scenario: Add product to the basket
    Given user is login
    When Click add to cart
    When Click delete product in basket
    Then Product is delete