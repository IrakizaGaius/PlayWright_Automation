import re
from playwright.sync_api import Page, expect


def test_options(page: Page) -> None:
    page.goto("https://demoqa.com/select-menu",timeout=60000)
    page.locator("#cars").select_option(["volvo", "saab", "audi"])
    page.locator("div").filter(has_text=re.compile(r"^Select\.\.\.$")).nth(2).click()
    page.locator("#react-select-4-option-2").click()
    page.locator("#react-select-4-option-0").click()
    page.locator("#oldSelectMenu").select_option("5")
    page.locator("#selectOne div").filter(has_text="Select Title").nth(1).click()
    page.get_by_text("Dr.", exact=True).click()
    page.get_by_text("Select Option").click()
    page.get_by_text("A root option", exact=True).click()
    expect(page.locator("#selectOne div").filter(has_text="Dr.").nth(1)).to_be_visible()
