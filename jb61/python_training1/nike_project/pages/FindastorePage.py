class FindastorePage:
    def __init__(self, page):
        self.page = page

    def find_adress(self, adress):
        print("Here you should put your adress")

        adress_input = self.page.locator('input[name="ta-Location_input"]')
        adress_input.wait_for(state="visible", timeout=10000)
        adress_input.fill(adress)

        self.page.wait_for_timeout(1000)

        print("The adress was filled successfully!")
        adress_input.press("Enter")

        self.page.wait_for_timeout(10000)
