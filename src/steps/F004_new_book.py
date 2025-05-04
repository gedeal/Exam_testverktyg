
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


@given(u'User chooses \'Add a book\'')
def login_add_book(context):
    #context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()    

    sleep(0)


@when(u'adds Title')
def add_title(context):
    context.page.get_by_test_id("add-book").click()
    expect(context.page.get_by_text(" Sidan för dig som gillar att läsa. Välj dina favoriter")).to_be_visible()
    context.page.get_by_test_id("add-input-title").fill("Gerson");
   # context.page.keyboard.press("Enter")

    sleep(0)

@when(u'adds writer')
def add_writer(context):
   
    expect(context.page.get_by_text(" Sidan för dig som gillar att läsa. Välj dina favoriter")).to_be_visible()
    context.page.get_by_test_id("add-input-author").fill("Writer Gerson");
   # context.page.keyboard.press("Enter")
    sleep(0)

@then(u'add the new book')
def add_book(context):
    context.page.get_by_test_id("add-submit").click()
    sleep(0)

@then(u'control if added book is in catalog')
def control_catalog(context):
    context.page.get_by_test_id("catalog").click();
    expect(context.page.get_by_text("Gerson\", Writer Gerson")).to_be_visible()
    sleep(0)
    