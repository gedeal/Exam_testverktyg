


#  Vad jag har testat

[Se STORIES.md](STORIES.md)


# hur startar projektet

### Installera verktyger

    python.exe -m pip install --upgrade pip
    pip install pytest-playwright
    playwright install
    pip install behave


# Användbara kommandon:

## Kör test
    clear | behave .\src

    clear | behave .\src\features\F001_login.feature 

    playwright codegen  "https://tap-ht24-testverktyg.github.io/exam-template/"


## Tips 
### väntetid på testet

    from time import sleep
    .
    sleep(0)

### välj mellan n:te platser
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")