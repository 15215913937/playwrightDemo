from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://bed.test.cnzxa.cn/#/login")
    page.goto("http://bed.test.cnzxa.cn/#/")
    page.goto("http://bed.test.cnzxa.cn/#/login")
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("qwe")
    page.get_by_placeholder("请输入用户名").click(button="right")
    page.locator("div").filter(has_text="Copyright2021 绍兴康特宝医疗科技有限责任公司").nth(2).click()
    page.get_by_placeholder("请输入用户名").click(button="right")
    page.get_by_placeholder("请输入用户名").click(button="right")
    page.get_by_text("智能床垫控制系统自动登录登 录").click()
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").click(button="right")
    page.get_by_text("智能床垫控制系统自动登录登 录").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
