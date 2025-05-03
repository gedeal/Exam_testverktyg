
Feature: Control choosen book in 'My list'
    *****  User can see the chosen book in 'my list'  ******

    Scenario: User log in to My books
        Given User chooses the 'My books' page
        Then  User see only the choosen book in list
        