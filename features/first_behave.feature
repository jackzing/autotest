Feature: My first behave feature

  Scenario: Add two numbers
    Given I have two integers a(10) and b (15)
    When I add the numbers
    Then I print the addition result(25)