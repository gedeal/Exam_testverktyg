from playwright.sync_api import sync_playwright
from time import sleep

def before_all (context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium

    #context.browser = context.browser_type.launch(headless=False,slow_mo=200)
    context.browser = context.browser_type.launch(headless=True)    ## No browser

    # Go to the starting url before each test.
    context.page = context.browser.new_page()
    context.base_url = "https://tap-ht24-testverktyg.github.io/exam-template/"
    context.page.goto(context.base_url) 


def before_scenario(context, scenario):
   #context.page = context.browser.new_page()
   context.base_url = "https://tap-ht24-testverktyg.github.io/exam-template/"
   # context.page.goto(context.base_url) 
   print ('') 


def after_scenario(context, scenario):
   print ('* end scenario run') 
    #if context.page:
     #   context.page.close()
 

def after_all(context):
    sleep(0)
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()