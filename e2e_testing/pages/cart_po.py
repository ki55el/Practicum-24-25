class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")

    def click_cart_button(self):
        self.cart_button.click()
