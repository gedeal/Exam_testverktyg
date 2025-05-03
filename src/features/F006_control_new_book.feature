Feature: Control choosen book in 'My list'
    *****  User can see the book list   ******

    Scenario: User control the books in the catalog
        Given the user is on the 'Läslistan' login page
        When the user has the following items to the catalog
            |book                                                  |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen  |
            | Kaffekokaren som visste för mycket                   |
            | Min katt är min chef                                 |
            | 100 sätt att undvika måndagar                        |
            | Gräv där du står – och hitta en pizzameny            |
            | Jag trodde det var tisdag                            |
            | Att prata med växter                                 |
        Then No books are marked (choosen)


        