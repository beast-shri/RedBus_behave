Feature: RedBus_facebook


  Scenario Outline:Signup icon should be present
    Given User should be able to launch the browser
    When User should be able to click on signup icon
    Then User should be able to click on signup link
    Then User should be able to click on Facebook link
    And user should be able to provide vaild email "<email>"
    Then user should be able to provide vaild password "<password>"
    And user should be able to click on login button


    Examples:
    |    email               |     password |
    |shrisharan1432@gmail.com|     shribeast|