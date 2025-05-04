
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


@given(u'User chooses the initial page')

def test_has_title(context):
   # context.page.goto(context.base_url)  

    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()
    expect(context.page.get_by_text('Sidan för dig som gillar att läsa')).to_be_visible()
    sleep(0)

@when(u'User browse the button options')
def check_buttons(context):

    context.page.get_by_test_id("add-book").click()
    expect(context.page.get_by_text('Titel')).to_be_visible()
    expect(context.page.get_by_text('Författare')).to_be_visible()

    context.page.get_by_test_id("favorites").click()
    expect(context.page.get_by_text('När du valt, kommer dina favoritböcker att visas här')).to_be_visible()

    sleep(0)


@then(u'first page is show')
def see_first_page(context):

    context.page.get_by_test_id("catalog").click()
    expect(context.page.get_by_text('Sidan för dig som gillar att läsa. Välj dina favoriter.')).to_be_visible()
    sleep(0)