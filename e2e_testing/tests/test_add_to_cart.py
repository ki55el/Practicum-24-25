from playwright.sync_api import expect

from pages.cart_po import CartPage
from pages.login_po import LoginPage
from pages.products_po import ProductsPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.click_add_to_cart_backpack()

    cart_page.click_cart_button()

    expect(cart_page.shopping_cart_badge).to_have_text('1')
