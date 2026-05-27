from playwright.sync_api import expect
import time

from PageObj.login import Login
from PageObj.register import Register



def test_register(context) -> None:
    browser_page = context.new_page()
    reg = Register(browser_page, context)
    page = reg.register()
    time.sleep(10)
    h1_locator = page.locator("h1")
    expect(h1_locator).to_contain_text("My account")




def test_login( context) -> None:
    login = Login(context)
    page = login.login()
    expect(page.get_by_text("Here you can manage your profile, favorites and orders.")).to_have_text(
        "Here you can manage your profile, favorites and orders.")
