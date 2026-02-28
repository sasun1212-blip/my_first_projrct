import random

class ResultsPage:
    def __init__(self,page):
        self.page = page

    def click_random_item(self):
            print("Beginning to search for random item")

            item_selector = ".product-card__link-overlay"

            product_links = self.page.locator(item_selector)

            items_count = product_links.count()
            print(f"Overall successfully found: {items_count}")

            if items_count > 0:
                random_index = random.randint(0, items_count - 1)
                print(f"Clicking on a item number {random_index + 1}")

                target_item = product_links.nth(random_index)

                target_item.scroll_into_view_if_needed()

                self.page.wait_for_timeout(1000)

                target_item.click(force=True)

                print("Waiting for the item to appear")
                self.page.wait_for_load_state("networkidle")
            else:
                raise Exception("Item isn't available (count = 0)")


