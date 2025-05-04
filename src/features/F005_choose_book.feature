
Feature: Choose a book
    *****  User can choose a book in the catalog ******

    Scenario: User chooses a book
        Given User chooses catalog page
        When  book list is shown
        Then  the chosen book exist in the list
        And   user chooses the book
        And   marking is permanent visible in list 