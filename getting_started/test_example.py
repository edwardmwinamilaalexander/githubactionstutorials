import re
from playwright.sync_api import Page, expect


# "page" belongs to an isolated BrowserContext, created for this specific test.
def test_has_title(page: Page):
    page.goto("https://edkofashion.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Edko Fashion"))

 # "page" in this second test is completely isolated from the first test.
def test_get_started_link(page: Page):
    page.goto("https://edkofashion.com/")

    # Click the shop link.
    page.get_by_role("link", name="Shop").first.click()

    # Expects page to have a heading with the name of Installation.
    expect(page.locator(".woocommerce-products-header__title.page-title")).to_be_visible()