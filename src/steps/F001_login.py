
from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep
from src.pages.search_page import SearchPage, LoginPage

@given(u'User chooses the initial page')

def test_has_title(context):
    LoginPage.startpage(context)


@when(u'User browse the button options')
def check_buttons(context):

    context.page.get_by_test_id("add-book").click()
    expect(context.page.get_by_text('Titel')).to_be_visible()
    expect(context.page.get_by_text('Författare')).to_be_visible()

    SearchPage.favorites(context)
    expect(context.page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")).to_be_visible()
    

@then(u'first page is show')
def see_first_page(context):
    LoginPage.catalogpage(context)