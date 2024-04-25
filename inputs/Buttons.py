import re
from playwright.sync_api import Page, expect


def test_doubleClick(page: Page) -> None:
    page.goto("/buttons", timeout=60000)
    page.get_by_role("button", name="Double Click Me").dblclick()
    expect(page.locator("#doubleClickMessage")).to_contain_text("You have done a double click")

def test_RightClick(page: Page) -> None:
    page.goto("/buttons", timeout=60000)
    page.get_by_role("button", name="Right Click Me").click(button="right")
    expect(page.locator("#rightClickMessage")).to_contain_text("You have done a right click")
    
def test_Click(page: Page) -> None:
    page.goto("/buttons", timeout=60000)
    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.locator("#dynamicClickMessage")).to_contain_text("You have done a dynamic click")


