Feature: Habrarating

  Scenario: Show a rating
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    Then I should see link contents url "habrahabr.ru"

  Scenario: Vote for a site
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    When I click link contents "+"
    Then I should see "Vote successful" somewhere in page

  Scenario: Vote for a site and look at the rating
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    Then I should see "Rating:7" somewhere in page
