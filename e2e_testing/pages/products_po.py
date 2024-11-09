class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.product_sort_container = page.locator("[data-test=\"product-sort-container\"]")
        self.inventory_item_price = page.locator("[data-test=\"inventory-item-price\"]")

    def click_add_to_cart_backpack(self):
        self.add_to_cart_backpack.click()

    def select_sort_lohi(self):
        self.product_sort_container.select_option("lohi")
