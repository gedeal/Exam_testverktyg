
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


@given(u'User logs in')
def login(context):
    context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")

    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()
    sleep(0)


@when(u'User chooses the my book list')
def choos_my_books(context):
    context.page.get_by_test_id("favorites").click()
    sleep(0)


@then(u'user has no book in list')
def list_empty(context):
    expect(context.page.get_by_text("Sidan för dig som gillar att")).to_be_visible()
    expect(context.page.get_by_text("När du valt, kommer dina")).to_be_visible()
    sleep(0)

@then(u'there is no booked marked in the catalog')
def control_catalog(context):
    context.page.get_by_test_id("catalog").click()

    pagecatalog = context.page.locator('.star selected')
    expect(pagecatalog).to_be_hidden();
    sleep(1)