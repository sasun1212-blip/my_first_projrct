from jb61.python_training1.nike_project.pages.WelcomePage import WelcomePage
from jb61.python_training1.nike_project.pages.search_page import SearchPage
class TestNikeTest():
    def test_search_for_item_and_getting_logo(self, setup_playwright_nike):
        page = setup_playwright_nike
        # logo = page.logo(page)
        welcome_page = WelcomePage(page)
        page.goto("https://www.nike.com/il/")
        welcome_page.click_on_women()
        # welcome_page.get_text_from_logo()
        page.locator("[href='https://www.nike.com/il/']").click()

        print ("dcdfd")

# welcome_page.click_on_close_popup()
        # welcom_page.search_for_irem()
        # logo_pafe.get.text_from_logo()

     def test_search_for_camera(self,):
          search_page = SearchPage(page)
          search_page.search_for_item("Air Jordan")
          text = search_page.get_amount_after_search()
          assert int(text) > 100, "products did not found "



