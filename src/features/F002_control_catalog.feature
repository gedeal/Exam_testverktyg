
Feature: Control the catalog content
    *****  User control the catalog content  ******

    Scenario Outline: User is logged and control the catalog content
        Given User veryfy if the right page shows
        When  User control "<book>" on the list
        Then  "<book>" in the list is market correct

        Examples:
            | book                                                 |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen  |
            | Kaffekokaren som visste för mycket                   |
            | Min katt är min chef                                 |
            | 100 sätt att undvika måndagar                        |
            | Gräv där du står – och hitta en pizzameny            |
            | Jag trodde det var tisdag                            |
            | Att prata med växter – och vad de egentligen tycker om dig |
