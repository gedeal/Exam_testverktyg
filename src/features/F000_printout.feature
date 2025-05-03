
Feature: Testing printouts
    *****  Behave can print out info  ******

    Scenario: User log in and print out info
        Given User logs to initial page
        When  There is more then 0 books in the list
        Then  User verify number of books in catalog
