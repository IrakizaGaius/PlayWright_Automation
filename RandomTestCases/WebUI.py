import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    """
    This function performs a series of actions on a web page.
    It navigates to a login page, enters credentials, logs in,
    and then performs a series of actions related to reports and ratings.

    Args:
        page (Page): The Playwright Page object to interact with the web page.

    Returns:
        None
    """

    # Navigate to the login page
    page.goto("https://stg.murakoze.rw/home/login")

    # Input username
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Clarisse")

    # Input password
    page.get_by_placeholder("Type Password").click()
    page.get_by_placeholder("Type Password").fill("TestingApp@123")

    # Click sign in button
    page.get_by_role("button", name="Sign in").click(timeout=60000)

    # Click reports button
    page.get_by_role("button", name="Reports ").click(timeout=60000)

    # Click downloadable reports link
    page.get_by_role("link", name="Downloadable Reports").first.click()

    # Verify that the general overview report is visible
    expect(page.get_by_text("GENERAL OVERVIEW This report")).to_be_visible(timeout=60000)

    # Verify that the branches performance report is visible
    expect(page.get_by_text("BRANCHES PERFORMANCE REPORT Detailed report of how every branch is doing in")).to_be_visible()

    # Verify that the services performance report is visible
    expect(page.get_by_text("SERVICES PERFORMANCE REPORT Detailed report of how every service is doing in")).to_be_visible()

    # Click reports button again
    page.get_by_role("button", name="Reports ").click()

    # Click performance report link
    page.get_by_role("link", name="Performance Report").click()

    # Verify that the performance report is visible
    expect(page.locator("div").filter(has_text="Performance Report Home Performance Report Wiredin choose Date range × Services").nth(3)).to_be_visible()

    # Click reports button again
    page.get_by_role("button", name="Reports ").click()

    # Click ratings link
    page.get_by_role("link", name="Ratings").click()

    # Click 10 link
    page.get_by_role("link", name="10").click()

    # Click view link for a rating
    page.get_by_role("row", name="2024-02-09 21:10:38 Excellent").get_by_label("View").click()

    # Click go to question link
    page.get_by_role("link", name=" Go to question").click()

    # Verify that the rating question is visible
    expect(page.locator(".az-content-body > div:nth-child(4) > div")).to_be_visible()
