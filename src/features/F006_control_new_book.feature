Feature: User add new books in 'My list' and control the inclusion
    *****  User can add and see the books list   ******

    Scenario Outline: User add books in the list
        Given User is on the 'Läslistan' login page
        When  User adds "<book>" and "<author>" in the list
        Then  the "<book>" and "<author>"  shows in the list

        Examples: Add books
            | book           | author               |
            | I was not here | Phanton of the Opera |
            | X-man | Marvel |
 
    Scenario Outline: User marks "<mark_book>" in the list
        Given User control the page info for "<mark_book>"
        When  User marks book: "<mark_book>" in the list
        Then  "<mark_book>" is market correct
                
        Examples: Marked books
            | mark_book   |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen  |
            | Min katt är min chef   |
            | I was not here  |

    Scenario Outline: User unmark books in the list
        Given  User unmarked book: "<unmark_book>" in the list
        Then  "<unmark_book>"  is market correct    

        Examples: Remove marked books
            | unmark_book      |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen  |
            | I was not here  |         