
from playwright.sync_api import  expect
import json

from PageObj.invoice import InvoicePage
from PageObj.login import Login



def intercept_response(route):
    response = {
    "current_page": 1,
    "data": [],
    "from": None,
    "last_page": 1,
    "per_page": 15,
    "to": None,
    "total": 0}
    route.fulfill(json = json.dumps(response))


def test_intercept_response(context):
    login = Login(context)
    page = login.login()
    expect(page.get_by_role("heading", level=1)).to_have_text("My account")
    inv =  InvoicePage(page)
    inv.create_invoice()

    page.route("https://api.practicesoftwaretesting.com/invoices?page=1", intercept_response)
    page.get_by_text("Home").click()
    page.locator("#menu").click()
    page.get_by_text("My invoices").click()
    assert page.locator("td").is_visible() is False