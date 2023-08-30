# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/30 9:10
import time

from playwright.sync_api import sync_playwright


def on_response(response):
    # print(f'Statue {response.status}: {response.url}')
    if '/api/sys/user/login' in response.url and response.status == 200:
        print(response.json())


# 方法返回的是一个 PlaywrightContextManager 对象，可以理解是一个浏览器上下文管理器，我们将其赋值为变量 p
with sync_playwright() as p:
    # 调用了 PlaywrightContextManager 对象的 chromium、firefox、webkit 属性依次创建了一个 Chromium、Firefox 以及 Webkit 浏览器实例
    # 接着用一个 for 循环依次执行了它们的 launch 方法
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # 同时设置了 headless 参数为 False,如果不设置为 False，默认是无头模式启动浏览器，我们看不到任何窗口
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.on('response', on_response)
        page.goto('http://bed.test.cnzxa.cn/#/login')
        page.screenshot(path=f'./screenshot/screenshot-{browser_type.name}.png')
        page.get_by_placeholder("请输入用户名").fill("admin")
        page.get_by_placeholder("请输入密码").fill("Admin!123")
        page.get_by_role("button", name="登 录").click()
        time.sleep(1)
        page.screenshot(path=f'./screenshot/screenshot1-{browser_type.name}.png')
        # page.get_by_text("undefined（admin）").click()
        # page.get_by_label("床垫名称").fill("创青春")
        # page.get_by_role("button", name="查 询").click()
        # time.sleep(5)
        # print(page.title())
        browser.close()
