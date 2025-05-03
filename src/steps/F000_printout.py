#import re

import logging

# Basic logging config --------
logging.basicConfig(
    level=logging.INFO,  # You can change to DEBUG if needed
    #level=logging.DEBUG,  # You can change to DEBUG if needed
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)
# ------------------------------

from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep

from playwright.sync_api import sync_playwright
from src.pages.search_page import SearchPage

book = "100 sätt att undvika måndagar"
book2= "Min katt är min chef"


@given(u'User logs to initial page')
def choose_catalog(context):
    context.page.goto(context.base_url)  
    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()    
    sleep(0)

@when(u'There is more then 0 books in the list')
def books_in_list(context):
    pagecatalog = context.page.locator('.book');
    expect(pagecatalog).not_to_have_count(0)

@then(u'User verify number of books in catalog')
def nr_of_bookd(context):

    count = context.page.locator('.book').count();
#   Print informations
    print(f'\n  ****TEST**** There are {count} books in the list')

    sleep(0)
