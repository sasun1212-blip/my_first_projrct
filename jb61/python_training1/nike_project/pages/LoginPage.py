class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_email_and_continue(self, email_address):
        print(f"Gmail: {email_address} ...")

        email_input = self.page.locator('#username')

        email_input.wait_for(state="visible")

        email_input.fill(email_address)

        print("Pressing 'Continue'...")

        continue_btn = self.page.get_by_role("button", name="Continue")

        continue_btn.wait_for(state="visible")
        continue_btn.click()

        self.page.wait_for_timeout(3000)