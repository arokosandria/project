Feature: Buy
  Scenario: Add product to the basket
    Given user is login
    When Click add to cart
    Then User see product in basket
  Scenario: Delete product to the basket
    When Go to the basket
    When Click delete product in basket
    Then Product is delete
  Scenario: Delete product in product list
    Given user is login
    When Click add to cart
    When Click remove in product list
    Then Product is delete in product list
  Scenario: Delete product in details
    Given user is login
    When Click add to cart
    When Click in product
    When Click remove in product details
    Then Product is delete in product details
  Scenario: View product in the basket
    Given user is login
    When Click add to cart
    When Go to the basket
    Then View product in basket
  Scenario: View products
    Given user is login
    When Click add to cart next product
    When Go to the basket
    Then View products in basket

  Scenario: shopping interruption
    Given user is login
    When Go to the basket
    When Click continue
    Then Login success

  Scenario: Bad delivery information
    When Go to the basket
    When Go to checkout
    When Fill First Name and Last_Name
    When Continue
    Then View error information

  Scenario: Good delivery information
    When Fill Zip
    When Continue
    Then Checkout
  Scenario: Cancel order
    When Click cancel
    Then Login success

  Scenario: Price order
    When Go to the basket
    When Go to checkout
    When Fill First Name and Last_Name
    When Fill Zip
    When Continue
    Then Price Order
  Scenario: Finish order
    When Click finish
    Then Finish

