
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep
from src.pages.search_page import SearchPage, LoginPage

@given(u'User logs in')
def login(context):
    LoginPage.startpage(context)

@when(u'User chooses the my book list')
def choos_my_books(context):
    SearchPage.favorites(context)

@then(u'there is no booked marked in the catalog')
def control_catalog(context):
    LoginPage.catalogpage(context)

    pagecatalog = context.page.locator('.star selected')
    expect(pagecatalog).to_be_hidden()
    sleep(0)