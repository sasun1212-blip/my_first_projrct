class WelcomePage:
    def __init__(self,page):
        self.page = page

    def click_on_women(self):
        women_btn = self.page.locator('a', has_text="Women").first
        women_btn.wait_for(state="visible", timeout=10000)
        women_btn.click()

        self.page.wait_for_url("**/women**", timeout=15000)
        print("successfully opened women page!")

    def click_on_logo(self):
        print("Pressing the button 'Logo'")

        logo_btn = self.page.locator('a[aria-label="Nike Homepage"]').first

        logo_btn.wait_for(state="visible", timeout=10000)
        logo_btn.click()

        # Ждем, пока URL снова станет главной страницей
        self.page.wait_for_url("https://www.nike.com/il/", timeout=15000)
        print("successfully came back to the main page!")


    def click_sign_in(self):
        print("pressing on the 'Sign In'")

        sign_in_btn = self.page.locator('a', has_text="Sign In").first

        sign_in_btn.wait_for(state="visible")
        sign_in_btn.click(force=True)

    def click_help(self):
        print("Pressing the button 'Help'...")

        help_link = self.page.locator('a', has_text="Help").first

        help_link.wait_for(state="visible", timeout=3000)
        help_link.click()
        print("successfully opened Help page!")

    def click_find_a_store(self):
        print("Pressing the find_a_store button")

        find_a_store_btn = self.page.locator('a', has_text="Find a Store").first
        find_a_store_btn.wait_for(state="visible", timeout=10000)
        find_a_store_btn.click()


