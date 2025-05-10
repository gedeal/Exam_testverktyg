
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep
from src.pages.search_page import SearchPage, LoginPage

@given(u'User chooses \'Add a book\'')
def login_add_book(context):
    LoginPage.startpage(context)


@when(u'adds Title')
def add_title(context):
    context.page.get_by_test_id("add-book").click()
    expect(context.page.get_by_text(" Sidan för dig som gillar att läsa. Välj dina favoriter")).to_be_visible()
    context.page.get_by_test_id("add-input-title").fill("Gerson")
    sleep(0)

@when(u'adds writer')
def add_writer(context):
    expect(context.page.get_by_text(" Sidan för dig som gillar att läsa. Välj dina favoriter")).to_be_visible()
    context.page.get_by_test_id("add-input-author").fill("Writer Gerson")
    sleep(0)

@then(u'add the new book')
def add_book(context):
    context.page.get_by_test_id("add-submit").click()
    sleep(0)

@then(u'control if added book is in catalog')
def control_catalog(context):
    LoginPage.catalogpage(context)

    expect(context.page.get_by_text("Gerson\", Writer Gerson")).to_be_visible()

    #   ToBeDone
    #   Need to erase entries = Refresh page
    #   otherwise this entry will cause fail in other tests 
    SearchPage.navigate(context)
    sleep(0)
    