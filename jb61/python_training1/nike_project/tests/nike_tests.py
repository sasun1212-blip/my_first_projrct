from jb61.python_training1.nike_project.pages.WelcomePage import WelcomePage
from jb61.python_training1.nike_project.pages.search_page import SearchPage
from jb61.python_training1.nike_project.pages.ResultsPage import ResultsPage
from jb61.python_training1.nike_project.pages.ProductPage import ProductPage
from jb61.python_training1.nike_project.pages.LoginPage import LoginPage
from jb61.python_training1.nike_project.pages.HelpPage import HelpPage
from jb61.python_training1.nike_project.pages.FindastorePage import FindastorePage

class TestNikeTest():
    def test_navigation_women_and_logo(self, setup_playwright_nike):
        page = setup_playwright_nike
        welcome_page = WelcomePage(page)

        page.goto("https://www.nike.com/il/")
        welcome_page.click_on_women()
        page.wait_for_timeout(1000)
        welcome_page.click_on_logo()


    def test_search(self, setup_playwright_nike):
        page = setup_playwright_nike
        search_page = SearchPage(page)
        results_page = ResultsPage(page)
        product_page = ProductPage(page)

        page.goto("https://www.nike.com/il/")
        search_page.search_for_item("Air Jordan")
        text = search_page.get_amount_of_items()

        assert int(text) > 0, "products not found"

        results_page.click_random_item()

        product_page.select_random_available_size()
        product_page.click_add_to_cart()

    def test_sign_in_flow(self, setup_playwright_nike):
        page = setup_playwright_nike
        welcome_page = WelcomePage(page)
        login_page = LoginPage(page)

        page.goto("https://www.nike.com/il/")

        welcome_page.click_sign_in()

        login_page.enter_email_and_continue("sasun1212@gmail.com")

    def test_help(self, setup_playwright_nike):
        page = setup_playwright_nike
        welcome_page = WelcomePage(page)
        help_page = HelpPage(page)

        page.goto("https://www.nike.com/il/")
        welcome_page.click_help()

        help_page.search_for_help("Where is my Nike order?")


    def test_findstore(self, setup_playwright_nike):
        page = setup_playwright_nike
        welcome_page = WelcomePage(page)
        findastore_page = FindastorePage(page)

        page.goto("https://www.nike.com/il/")

        welcome_page.click_find_a_store()

        findastore_page.find_adress("Ir Yamim, Netanya, Israel")




