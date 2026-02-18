import time

from torch._prims import item

from jb.paython_training.playwright_example.my_first_test import search_menu


class SearchPage():
    def __init__(self,page):
        self.page = page

    def search_for_item(self):
        search_menu = self.page.locator("['id=gn-search-input']")
        search_menu_short = self.page.locator("[id='gn-search-input']")

        search_menu.click()
        search_menu.fill(item)

        self.page.get_by_role("button", name="Search").click()

