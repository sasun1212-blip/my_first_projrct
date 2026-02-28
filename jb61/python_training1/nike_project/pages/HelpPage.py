class HelpPage:
    def __init__(self, page):
        self.page = page

    def search_for_help(self, question):
        print(f"Here is the question: '{question}'...")

        search_input = self.page.locator('input[type="text"]').first

        search_input.wait_for(state="visible", timeout=15000)

        search_input.click()

        self.page.wait_for_timeout(500)

        search_input.press_sequentially(question, delay=100)

        print("The question was correct!")
        search_input.press("Enter")

        self.page.wait_for_timeout(3000)


