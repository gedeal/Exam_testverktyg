
Feature: Choose a book
    *****  User can choose a book in the catalog ******

    Scenario: User chooses a book
        Given User chooses catalog
        When  book list is shown
        Then  the chosen book exist in the list
        And   user chooses the chosen book
        And   marking is permanent visible