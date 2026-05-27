from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

import time
class Login:
    def __init__(self, context):
        self.context = context

    def login(self):
        browser_page = self.context.new_page()
        browser_page.goto("https://practicesoftwaretesting.com")
        browser_page.locator("#menu").click()
        browser_page.keyboard.down("Tab")
        browser_page.keyboard.press("Enter")
        h1_locator = browser_page.locator("h1")
        expect(h1_locator).to_contain_text("My account")


        return browser_page

