class SearchPage:
    def __init__(self,page):
        self.page = page

    def search_for_item(self, item):
        self.page.query_selector_all(".nav-css-tr0r01")[0].click()
        search_menu = self.page.locator("[id='gn-search-input']")
        search_menu.fill(item)
        search_menu.press("Enter")

        self.page.wait_for_url("**/*q=*", timeout=10000)

    def get_amount_of_items(self):
        print("trying to get result")

        title_locator = self.page.locator("h1")

        title_locator.first.wait_for(state="visible")

        text = title_locator.first.inner_text()
        print(f"DEBUG: '{text}'")

        import re
        numbers = re.findall(r'\d+', text)

        final_count = numbers[0] if numbers else "0"
        print(f"DEBUG: The item found: {final_count}")

        return final_count

