
import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from time import sleep


def test_has_title(context):
   # context.page.goto(context.base_url)  
    print ('Start Tests')

def check_buttons(context):

    page.get_by_test_id("add-book").click()
    expect(page.get_by_text('Titel')).to_be_visible()
    expect(page.get_by_text('Författare')).to_be_visible()

    SearchPage.favorites(context)
    expect(page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")).to_be_visible()
       

