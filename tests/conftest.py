import  pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture
def context(playwright, request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    else:
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(storage_state="playwright/.auth/state.json")
    yield context
    context.clear_cookies(path="../playwright/.auth/state.json")
    browser.close()
