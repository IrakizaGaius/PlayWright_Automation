import asyncio
from playwright.async_api import async_playwright, expect
import pytest

@pytest.mark.asyncio
async def test_checkBox():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox", timeout=60000)
        # Actions
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="screenshots/checkboxes.png")
        
        #assertions
        await page.is_checked('label[for="tree-node-home"]') is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
        
        #stop--Tracing
        await context.tracing.stop(path= "logs/trace.zip")
        
        #Close Browser
        await browser.close()
        
asyncio.run(test_checkBox())
                     