from playwright.sync_api import expect

from pages.login_po import LoginPage
from pages.products_po import ProductsPage

def test_product_sort(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.select_sort_lohi()

    expect(products_page.inventory_item_price).to_have_text(['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99'])
