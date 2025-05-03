


#  What I have tested

See : [STORIES.md](STORIES.md)


# How to start the project

### Install tools

    python.exe -m pip install --upgrade pip
    pip install pytest-playwright
    playwright install
    pip install behave


# Usefull commands:

## Run behave test
- Run all tests

        clear | behave .\src

- Run specific test

        clear | behave src\features\F001_login.feature 

## Run pytests

        clear | pytest -v       
        
## Run codegen

        playwright codegen  "https://tap-ht24-testverktyg.github.io/exam-template/"


-----

# Tips 
### väntetid på testet

    from time import sleep
    .
    sleep(0)

### välj mellan n:te platser
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")