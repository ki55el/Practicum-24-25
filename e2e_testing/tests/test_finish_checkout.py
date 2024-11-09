from playwright.sync_api import expect

from pages.cart_po import CartPage
from pages.checkout_po import CheckoutPage
from pages.login_po import LoginPage
from pages.products_po import ProductsPage

def test_finish_checkout(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.click_add_to_cart_backpack()

    cart_page.click_cart_button()
    
    checkout_page.click_checkout_button()
    checkout_page.checkout("firstName", "lastName", "postalCode")
    checkout_page.finish()

    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
