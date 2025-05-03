
Feature: Control the catalog content
    *****  User control the catalog content  ******

    Scenario: User is logged and control the catalog content
        Given User veryfy if the right page shows
        When  User control the list
        Then  names in the list are correct