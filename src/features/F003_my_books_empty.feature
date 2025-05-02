
Feature: My books list - empty
    *****  User controls if his book list is enmpty  ******

    Scenario: User log in to my book list
        Given User logs in
        When  User chooses the my book list
        Then  user has no book in list
        Then  there is no booked marked in the catalog
     