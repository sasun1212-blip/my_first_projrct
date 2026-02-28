import random

class ProductPage:
    def __init__(self, page):
        self.page = page

    def select_random_available_size(self):
        print("Searching for the sizes...")

        all_inputs = self.page.locator('input[name="grid-selector-input"]')
        all_labels = self.page.locator('input[name="grid-selector-input"] ~ label')


        all_labels.first.wait_for(state="visible", timeout=10000)

        total_sizes = all_labels.count()
        available_indices = []

        print(f"Overall size count is (including unavailable once): {total_sizes}")


        for i in range(total_sizes):
            current_input = all_inputs.nth(i)
            current_label = all_labels.nth(i)

            if not current_label.is_visible():
                continue

            if current_input.is_disabled():
                continue

            if current_input.get_attribute("aria-disabled") == "true":
                continue

            available_indices.append(i)

        print(f"The available one: {len(available_indices)}")

        if not available_indices:
            raise Exception("There is no available one!")

        import random
        random_index = random.choice(available_indices)

        print(f"Clicking on the available one")
        target_label = all_labels.nth(random_index)
        target_label.scroll_into_view_if_needed()

        target_label.click(force=True)

        self.page.wait_for_timeout(1000)

    def click_add_to_cart(self):
        print("Adding it to the cart")

        add_to_cart_btn = self.page.locator('button[data-testid="atb-button"]')

        add_to_cart_btn.wait_for(state="visible", timeout=10000)

        add_to_cart_btn.scroll_into_view_if_needed()
        add_to_cart_btn.click(force=True)

        print("Everything is done!")

        self.page.wait_for_timeout(4000)