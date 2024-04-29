import re
from playwright.sync_api import Page, expect


def test_Exploration(page: Page) -> None:
    page.goto("https://davidgoggins.com/",timeout=60000)
    page.locator("#menu-item-16").get_by_role("link", name="ACHIEVEMENTS").click()
    expect(page.get_by_role("link", name="IN THE MEDIA")).to_be_visible()
    page.get_by_role("link", name="IN THE MEDIA").click()
    expect(page.get_by_role("heading", name="goggins IN THE MEDIA")).to_be_visible()
    with page.expect_popup() as page1_info:
        page.locator(".read_link").first.click()
    page1 = page1_info.value
    page1.close()
    expect(page.get_by_role("link", name="ABOUT DAVID")).to_be_visible()
    page.goto("https://davidgoggins.com/about/",timeout=60000)
    expect(page.locator("#menu-item-15").get_by_role("link", name="ABOUT")).to_be_visible()
    expect(page.locator("#footer_menu").get_by_role("link", name="4X4X48")).to_be_visible()
