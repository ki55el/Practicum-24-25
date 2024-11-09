class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.firstName = page.locator("[data-test=\"firstName\"]")
        self.lastName = page.locator("[data-test=\"lastName\"]")
        self.postalCode = page.locator("[data-test=\"postalCode\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.complete_header = page.locator("[data-test=\"complete-header\"]")

    def click_checkout_button(self):
        self.checkout_button.click()
    
    def checkout(self, firstName, lastName, postalCode):
        self.firstName.fill(firstName)
        self.lastName.fill(lastName)
        self.postalCode.fill(postalCode)
        self.continue_button.click()
    
    def finish(self):
        self.finish_button.click()
