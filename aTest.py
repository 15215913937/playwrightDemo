# coding = utf-8
# Author: Shenbq
# Date: 2022/12/2 13:27
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        print(page.title())
        browser.close()
