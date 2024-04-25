import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone XR"]}


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/checkbox")
    expect(page.locator("span").filter(has_text="Home").first).to_be_visible()
    page.locator("span").filter(has_text="Home").first.click()
    expect(page.locator("#result")).to_be_visible()
