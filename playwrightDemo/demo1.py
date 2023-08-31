# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/30 9:10
import time

import playwright
import yaml
from playwright.sync_api import sync_playwright


def on_response(response):
    # print(f'Statue {response.status}: {response.url}')
    if '/api/sys/user/login' in response.url and response.status == 200:
        print(response.json()['data'])


def read_yml(yml_file_path):
    with open(yml_file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


data = read_yml('./data.yml')
LOGIN_RIGHT = (data['login']['right_username']['username'], data['login']['right_username']['password'])
BASE_URL = data['BASE_URL']
EXPECT_URL = data['expect_login_success_to_url']
# 方法返回的是一个 PlaywrightContextManager 对象，可以理解是一个浏览器上下文管理器，我们将其赋值为变量 p
with sync_playwright() as p:
    # 调用了 PlaywrightContextManager 对象的 chromium、firefox、webkit 属性依次创建了一个 Chromium、Firefox 以及 Webkit 浏览器实例
    # 接着用一个 for 循环依次执行了它们的 launch 方法
    # p.chromium.launch(headless=False)
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # 同时设置了 headless 参数为 False,如果不设置为 False，默认是无头模式启动浏览器，我们看不到任何窗口
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        # page.on('response', on_response)
        page.goto(BASE_URL + '/login')
        page.screenshot(path=f'./screenshot/login-{browser_type.name}.png')
        page.get_by_placeholder("请输入用户名").fill(LOGIN_RIGHT[0])
        page.get_by_placeholder("请输入密码").fill(LOGIN_RIGHT[1])
        page.get_by_role("button", name="登 录").click()
        page.screenshot(path=f'./screenshot/login_input-{browser_type.name}.png')
        page.wait_for_load_state('networkidle')
        page.wait_for_selector('.name')
        print(page.url)
        real_url = page.url
        assert EXPECT_URL in real_url
        page.screenshot(path=f'./screenshot/login_success-{browser_type.name}.png')
        # page.get_by_text("undefined（admin）").click()
        # page.get_by_label("床垫名称").fill("创青春")
        # page.get_by_role("button", name="查 询").click()
        # time.sleep(5)
        # print(page.title())
        browser.close()
