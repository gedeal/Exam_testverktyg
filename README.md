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

        clear | behave .\src --no-capture 

- Run specific test

        clear | behave src\features\F001_login.feature  --no-capture 

## Run pytests

        clear | pytest -v 
        
## Run codegen

        playwright codegen  "https://tap-ht24-testverktyg.github.io/exam-template/"


-----

# Tips 
### Clear terminal
    clear   # =>  VScode / PyCharm
    cls     # =>  Intellij

### Use print commands
behave captures stdout by default. To see raw print() output, disable capturing:

    behave --no-capture

### delay time inside test

    from time import sleep
    :
    sleep(1)   # 1 sec

### choose the nth: place
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")