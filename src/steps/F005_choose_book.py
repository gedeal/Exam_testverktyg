from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep

from src.pages.search_page import SearchPage

book = "100 sätt att undvika måndagar"
book2= "Min katt är min chef"


@given(u'User chooses catalog page')
def choose_catalog(context):
    context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()    

    sleep(0)


@when(u'book list is shown')
def book_list(context):

    pagecatalog = context.page.locator('.book');
    expect(pagecatalog).not_to_have_count(0)
    sleep(0)


@then(u'the chosen book exist in the list')
def choose_book_exist(context):

    expect(context.page.get_by_text(book)).to_be_visible()
    sleep(0)

@then(u'user chooses the book')
def choose_book(context):

    context.page.get_by_text(book).click()
    context.page.get_by_test_id("star-"+book).click()

    sleep(0)

@then(u'marking is permanent visible in list')
def marking_visible(context):

    # Get the element by test ID and Expect the element to have a specific class (exact match)
    element = context.page.get_by_test_id('star-'+book)
    expect(element).to_have_class('star selected')

    # Get the element by test ID and Expect the element to have a specific class (exact match)
    element = context.page.get_by_test_id('star-'+book2)
    expect(element).not_to_have_class('star selected')

    sleep(0)
 