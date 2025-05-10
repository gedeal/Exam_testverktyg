import re
from playwright.sync_api import expect
from time import sleep


class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("#search-input")

    def navigate(self):
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
        sleep(0)


    def search_for(self, query):
        expect(self.page).to_have_title(re.compile(query))


    def get_by(self, type, txt):
        self.page.get_by_role(type, name=txt).click()
        sleep(0)

    def favorites(self):
        self.page.get_by_test_id("favorites").click()
        expect(self.page.get_by_text("Sidan för dig som gillar att läsa. Välj dina favoriter.")).to_be_visible()
        sleep(0)


    def console_out(txt):
        print(txt)

class LoginPage:
    def startpage(self):
        self.page.get_by_role("heading", name="Läslistan")
        expect(self.page.get_by_role("heading", name="Välkommen!")).to_be_visible()  
        expect(self.page.get_by_text('Sidan för dig som gillar att läsa. Välj dina favoriter.')).to_be_visible()
  
        sleep(0)  

    def catalogpage(self):   
        self.page.get_by_test_id("catalog").click()
        expect(self.page.get_by_text('Sidan för dig som gillar att läsa. Välj dina favoriter.')).to_be_visible()
        