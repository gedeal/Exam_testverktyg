from behave import given, when, then
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep

from src.pages.search_page import SearchPage


@given(u'User is on the \'Läslistan\' login page')
def choose_catalog(context):
    #context.page.goto(context.base_url)    # Reset page

    context.page.get_by_role("heading", name="Läslistan")
    expect(context.page.get_by_role("heading", name="Välkommen!")).to_be_visible()    

    sleep(0)

@when(u'User adds "{book}" and "{author}" in the list')
def add_book(context, book, author):
    context.page.get_by_test_id("add-book").click()
    expect(context.page.get_by_text(" Sidan för dig som gillar att läsa. Välj dina favoriter")).to_be_visible()

    context.page.get_by_test_id("add-input-title").fill(f"{book}")
    context.page.get_by_test_id("add-input-author").fill(f"{author}")

    print (f"Book :---->   {book}")
    print (f"author:---->   {author}")
    context.page.get_by_test_id("add-submit").click()
    context.page.get_by_test_id("favorites").click()
    sleep(0)


@then(u'the "{book}" and "{author}"  shows in the list')
def control_add_book(context, book, author):
    context.page.get_by_test_id("catalog").click()
    expect(context.page.get_by_text(f'"{book}", {author}')).to_be_visible()
    sleep(0)


#--------------------------------------

@given(u'User control the page info for "{mark_book}"')
def step_impl(context, mark_book):
    sleep(0)
    expect(context.page.get_by_text(f'"{mark_book}"')).to_be_visible()


@when(u'User marks book: "{mark_book}" in the list')
def step_impl(context, mark_book):
    book = 'star-'+(f'{mark_book}')
    context.page.get_by_test_id(book).click()
    sleep(0)

@then(u'"{mark_book}" is market correct')
def step_impl(context, mark_book):
    book = 'star-'+(f'{mark_book}')
    element = context.page.get_by_test_id(book)
    expect(element).to_have_class('star selected')
    sleep(0)

# ------------------------------


@given(u'User unmarked book: "{unmark_book}" in the list')
def unmark_books(context,unmark_book):
    book = 'star-'+(f'{unmark_book}')
    context.page.get_by_test_id(book).click()
    sleep(0)

@then(u'"{unmark_book}"  is market correct')
def control_unmarked(context,unmark_book):
    book = 'star-'+(f'{unmark_book}')
    #print ('**** '+book)
    element = context.page.get_by_test_id(book)
    expect(element).not_to_have_class('star selected')

# control remaining marked book
    context.page.get_by_test_id("add-book").click()
    context.page.get_by_test_id("catalog").click()

    markedelement = context.page.get_by_test_id('star-Min katt är min chef')
    expect(markedelement).to_have_class('star selected')
    sleep(0)
