
Feature: Add a new book in list
    *****  User adds a new book in his list and see it in the catalog  ******

    Scenario: Add a new book in list
        Given User chooses 'Add a book'
        When  adds Title
        And   adds writer
        Then  add the new book
        And   control if added book is in catalog