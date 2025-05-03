
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


@given(u'User veryfy if the right page shows')
def step_control_right_page(context):
    context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")

    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()
    expect(context.page.get_by_text("Sidan för dig som gillar att")).to_be_visible()


@when(u'User control the list')
def control_list(context):
    expect(context.page.get_by_text("Hur man tappar bort sin TV")).to_be_visible()
    expect(context.page.get_by_text("Kaffekokaren som visste fö")).to_be_visible()
    expect(context.page.get_by_text("Min katt är min chef")).to_be_visible()
    expect(context.page.get_by_text("100 sätt att undvika må")).to_be_visible()
    expect(context.page.get_by_text("Gräv där du står")).to_be_visible()
    expect(context.page.get_by_text("Jag trodde det var tisdag")).to_be_visible()
    expect(context.page.get_by_text("Att prata med växter")).to_be_visible()

    sleep(1)

@then(u'names in the list are correct')
def contro_books_not_selected(context):

    #context.page.get_by_text("star-Jag trodde det var tisdag")
    locator = context.page.get_by_test_id("star-Jag trodde det var tisdag")

    expect(locator).not_to_have_class("star selected")
    locator.click()
    expect(locator).to_be_visible()
    expect(locator).to_have_class("star selected")

    sleep(3)
