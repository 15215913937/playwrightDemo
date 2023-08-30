import time

from playwright.sync_api import Playwright, sync_playwright, expect


def on_response(response):
    if '/api/sys/user/login' in response.url and response.status == 200:
        print(response.json())


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.on('response', on_response())
    page.goto("http://bed.test.cnzxa.cn/#/")
    page.get_by_placeholder("请输入用户名").fill("admin")
    page.get_by_placeholder("请输入密码").fill("Admin!123")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("undefined（admin）").click()
    page.get_by_label("床垫名称").fill("创青春")
    page.get_by_role("button", name="查 询").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
