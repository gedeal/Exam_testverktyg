from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep
from src.pages.search_page import SearchPage, LoginPage


@given(u'User logs to initial page')
def choose_catalog(context):
    LoginPage.startpage(context)

@when(u'There is more then 0 books in the list')
def books_in_list(context):
    pagecatalog = context.page.locator('.book')
    expect(pagecatalog).not_to_have_count(0)

@then(u'User verify number of books in catalog')
def nr_of_bookd(context):

    count = context.page.locator('.book').count()
#   Print informations
    print(f'\n  ****TEST**** There are {count} books in the list')
    sleep(0)
