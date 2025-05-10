import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


def test_login(context) -> None:
    
  #  browser = playwright.chromium.launch(headless=False)
  #  context = browser.new_context()
    page = context.new_page()
  #  page.on('console', lambda msg: print(msg.text()))

    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
   

    page.get_by_role("heading", name="Läslistan")
    expect(page.get_by_role("heading", name="Välkommen!")).to_be_visible()
 #  expect(page.get_by_text('Sidan för dig som gillar att läsa')).to_be_visible()
 

    sleep(0)

def test_list(context) -> None:
    
  #  browser = playwright.chromium.launch(headless=False)
  #  context = browser.new_context()
  #  page = context.new_page()
  #  page.on('console', lambda msg: print(msg.text()))

    page = context.new_page()
    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
   

    expect(page.get_by_text('Sidan för dig som gillar att läsa')).to_be_visible()
 

    page.get_by_test_id("add-book").click()
    expect(page.get_by_text('Titel')).to_be_visible()
    expect(page.get_by_text('Författare')).to_be_visible()

    page.get_by_test_id("favorites").click()
    expect(page.get_by_text("Sidan för dig som gillar att läsa. Välj dina favoriter.")).to_be_visible()
    sleep(0)

    expect(page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")).to_be_visible()
    sleep(0)

