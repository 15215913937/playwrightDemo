# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/30 9:33

from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 打开登录页面
    page.goto('http://bed.test.cnzxa.cn/#/login')
    page.screenshot(path=f'./screenshot/screenshot1.png')
    # 输入用户名、密码
    page.fill('//*[@id="name"]', 'admin')
    page.fill('//*[@id="password"]', 'Admin!123')
    # page.get_by_placeholder("请输入用户名").fill("admin")
    # page.get_by_placeholder("请输入密码").fill("Admin!1123")

    # 点击登录按钮
    page.get_by_role("button", name="登 录").click()

    # 打印出当前URL,用于验证是否登录成功
    print(page.url)

    # 关闭浏览器
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
