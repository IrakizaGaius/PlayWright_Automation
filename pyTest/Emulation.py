import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone XR"]}


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"inventory-list\"] div").filter(has_text="Sauce Labs Bolt T-ShirtGet").nth(1)).to_be_visible()
    expect(page.locator("[data-test=\"product-sort-container\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
