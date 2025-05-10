from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep
from src.pages.search_page import SearchPage, LoginPage

@given(u'User veryfy if the right page shows')
def step_control_right_page(context):
  #  context.page.goto(context.base_url)  
    LoginPage.startpage(context)

@when(u'User control "{book}" on the list')
def control_list(context, book):
    expect(context.page.get_by_text(f"{book}")).to_be_visible()
    sleep(0)

@then(u'"{book}" in the list is market correct')
def control_book_not_selected(context, book):
    bookstring =(f"star-{book}")

    locator = context.page.get_by_test_id(bookstring)
    expect(locator).not_to_have_class("star selected")
    locator.click()
    expect(locator).to_be_visible()
    expect(locator).to_have_class("star selected")

    sleep(0)
