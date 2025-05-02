import re
from asyncio import timeout
from time import sleep

from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_login(context) -> None:
    
  #  browser = playwright.chromium.launch(headless=False)
  #  context = browser.new_context()
    page = context.new_page()
  #  page.on('console', lambda msg: print(msg.text()))

    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
   

    page.get_by_role("heading", name="Läslistan")
    expect(page.get_by_role("heading", name="Välkommen!")).to_be_visible()
 #  expect(page.get_by_text('Sidan för dig som gillar att läsa')).to_be_visible()
 

    sleep(1)

def test_list(context) -> None:
    
  #  browser = playwright.chromium.launch(headless=False)
  #  context = browser.new_context()
  #  page = context.new_page()
  #  page.on('console', lambda msg: print(msg.text()))

    page = context.new_page()
    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
   

    expect(page.get_by_text('Sidan för dig som gillar att läsa')).to_be_visible()
 

    sleep(1)

