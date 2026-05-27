from .credentials import Credentials
from errno import ECHILD
import os
import pytest
import re
from playwright.sync_api import Playwright, expect
import time
class Register:
    def __init__(self, browser_page, context):
        self.browser_page = browser_page
        self.context = context

    def register(self):
        self.browser_page.goto("https://practicesoftwaretesting.com/")
        self.browser_page.get_by_text("Sign in").click()
        self.browser_page.get_by_label("Register your account").click()
        credentials = Credentials()
        username = credentials.generate_email()
        password = credentials.generate_password()

        self.browser_page.locator("#first_name").fill(username)
        self.browser_page.locator("#last_name").fill(password)

        self.browser_page.get_by_placeholder("YYYY-MM-DD").fill("1991-01-01")
        self.browser_page.locator("#country").select_option("India")
        self.browser_page.get_by_placeholder("Your Postcode *").fill("16046")

        self.browser_page.get_by_placeholder("e.g. 42 *").fill("10")
        self.browser_page.locator("#street").fill("2303 Pointe View Drive")
        self.browser_page.locator("#city").fill("Mars")
        self.browser_page.locator("#state").fill("PA")
        self.browser_page.locator("#phone").fill("9922921330")
        self.browser_page.locator("#email").fill(username)
        self.browser_page.locator("#password").fill(password)
        self.browser_page.get_by_text("Register").click()
        self.check_registration(username, password)

        return self.browser_page

    def check_registration(self,username, password):
        time.sleep(2)
        self.browser_page.locator("#email").fill(username)
        self.browser_page.get_by_placeholder("Your password").fill(password)
        self.browser_page.locator(".btnSubmit").click()
        expect(self.browser_page.get_by_text("Here you can manage your profile, favorites and orders.")).to_have_text(
                "Here you can manage your profile, favorites and orders.")
        time.sleep(12)
        auth_dir = "playwright/.auth"
        os.makedirs(auth_dir, exist_ok=True)
        self.context.storage_state(path=f"{auth_dir}/state.json")
