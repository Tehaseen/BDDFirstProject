Feature: GigaStore Login

  Scenario: Login to GigaStore with valid parameters
    Given launch Chrome browser
    When open GigaStore Homepage
    And Enter username "t.m@tm.tm" and password "Qwerty12345"
    And Click on login button
    Then User must successfully login to the Dashboard page
