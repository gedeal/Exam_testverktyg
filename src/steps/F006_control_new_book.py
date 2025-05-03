from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep

from playwright.sync_api import sync_playwright
from src.pages.search_page import SearchPage

@given(u'the user is on the \'Läslistan\' login page')
def step_impl(context):
    context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()    

    sleep(0)

@when(u'the user has the following items to the catalog')
def step_impl(context):
    pagecatalog = context.page.locator('.book');

    
@then(u'No books are marked (choosen)')
def step_impl(context):
    count = context.page.locator('.book').count();
    #   Print informations
    print(f'\n  **** There are {count} books in the list')