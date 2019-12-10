Feature: Product
  Scenario: Picture product
    Given user is login
    When click product
    Then User see pricture product
    Then User see title product
    Then User see description product
    Then User see price product
