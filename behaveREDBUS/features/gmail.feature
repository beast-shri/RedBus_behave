Feature: RedBus_gmail


  Scenario Outline:Signup icon should be present
    Given User should be able to launch the browser
    When User should be able to click on signup icon
    Then User should be able to click on signup link
    Then User should be able to click on gmail link
    Then user should be able to enter email "<gmail>"
    Then user should be able to click om next button
    Then user should be able to enter password "<password>"

    Examples:
    |        gmail            |          password      |
    | shrisharan1432@gmail.com|          shribeast