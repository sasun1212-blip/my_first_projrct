from os import link


class WelcomePage():

    def __init__(self,page):
        self.page = page

    def search_for_item(self):
        print ("trying to search fopr item")
        search_icon = self.page.locator("[id='header-search']")
        search_icon.click()
        locetors = self.page.query_selector_all("[name='q']")
        search_menu = locetors[1]
        search_menu.click()
        search_menu.fill("Shirt")

    def click_on_women(self):
        print("clicking on item")
        click_icon = self.page.locator("[href='https://www.nike.com/il/women']")
        click_icon.click()

    def click_on_logo(self):
        print("clicking on logo")
        self.page.get_by_role("Link", name="Nike Homepage").click()


    def get_text_from_logo(self):
        elements = self.page.query_selector_all("[class='product__grid__title gt-p']")
        elements_short= elements[0:5]
        for element in elements_short:
            text = element.inner_text()
            print (text)
            assert "Shoes" in text


    def click_on_close_popup(self):
        self.page.locator("[class='spicegems_cr_icon_close_Svg']").click()
