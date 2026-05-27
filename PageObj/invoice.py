import time

from playwright.sync_api import expect


class InvoicePage:
    def __init__(self, page):
        self.page = page
    def create_invoice(self):
        self.page.get_by_text("Home").click()
        self.page.get_by_text(" Combination Pliers ").click()
        self.page.locator(".btn-success").click()
        self.page.locator("#lblCartCount").click()
        self.page.get_by_role("button", name = "Proceed to checkout").click()
        self.page.get_by_role("button", name="Proceed to checkout").click()

        self.page.locator("#country").select_option("India")
        self.page.get_by_placeholder("Your Postcode *").fill("16046")
        self.page.keyboard.down("Tab")
        time.sleep(1)

        self.page.get_by_placeholder("e.g. 42 *").press_sequentially('42')
        time.sleep(1)
        self.page.locator("#street").fill("2303 Pointe View Drive")
        self.page.locator("#city").fill("Mars")
        self.page.locator("#state").fill("PA")
        self.page.get_by_role("button", name="Proceed to checkout").click()

        self.page.locator("#payment-method").select_option("cash-on-delivery")
        time.sleep(2)
        self.page.get_by_role("button", name= "Confirm").click()
        expect(self.page.locator(".help-block")).to_have_text("Payment was successful")
        self.page.get_by_role("button", name="Confirm").click()
        expect(self.page.locator("#order-confirmation")).to_contain_text("Thanks for your order!")
        time.sleep(2)