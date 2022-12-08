# coding = utf-8
# Author: Shenbq
# Date: 2022/8/11 13:22

import time
import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options

import opYml


class LoginCase(unittest.TestCase):
    # 测试数据
    correctUserAccount = opYml.getUserYml()['CorrectUserAccount']
    wrongUserAccount = opYml.getUserYml()['WrongUserAccount']
    # 截图地址
    successScreenCapPath = opYml.getCommonYml()['logAddress']['success']
    errorScreenCapPath = opYml.getCommonYml()['logAddress']['error']
    USERNAME_LOCATOR = "name"
    PASSWORD_LOCATOR = "password"
    LOGIN_BUTTON_LOCATOR = '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[5]/div/div/span/button'
    SEARCH_KEY_LOCATOR = 'name'
    BASE_URL = "http://bed.test.cnzxa.cn"


    @classmethod
    def setUpClass(cls) -> None:
        print("智能床垫后台登录模块测试开始----")

    def setUp(self):
        print("当前用例开始执行")
        options = Options()
        # 窗口最大化
        # self.driver.maximize_window()
        # 最大化启动
        options.add_argument('--start-maximized')
        # 禁用inforbar 当前使用无效，原因尚不明确
        options.add_argument('--disable-infobars')
        # 指定浏览器
        self.driver = webdriver.Chrome(options=options)
        # 指定打开页面地址
        self.driver.get(self.BASE_URL)


        self.driver.implicitly_wait(5)

    # 定义登录方法
    def login(self, username, password):
        driver = self.driver
        driver.find_element_by_id(self.USERNAME_LOCATOR).clear()
        driver.find_element_by_id(self.PASSWORD_LOCATOR).clear()
        sleep(1)
        driver.find_element_by_id(self.USERNAME_LOCATOR).send_keys(username)
        driver.find_element_by_id(self.PASSWORD_LOCATOR).send_keys(password)
        driver.find_element_by_xpath(self.LOGIN_BUTTON_LOCATOR).click()

    def test_login_success(self):
        # 获取格式化的当前时间
        ran_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        '''用户名、密码正确'''
        self.login(self.correctUserAccount['username'], self.correctUserAccount['password'])
        username = self.driver.find_element_by_class_name(self.SEARCH_KEY_LOCATOR)
        # 截图  可自定义截图后的保存位置和图片命名
        self.driver.get_screenshot_as_file(self.successScreenCapPath + "\\success_login_" + ran_str + ".png")
        self.assertTrue(self.correctUserAccount['username'] in username.text)

    def test_login_pwd_error(self):
        '''密码不正确'''
        self.login(self.wrongUserAccount[0]['username'], self.wrongUserAccount[0]['password'])
        sleep(2)
        logInfo = '错误密码'
        self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
        alert_info = self.driver.find_element_by_xpath('/html/body/div[2]/span/div/div/div/span')
        self.assertIn('用户信息有误', alert_info.text)

    # def test_login_pwd_space(self):
    #     '''密码不正确-空格'''
    #     self.driver.find_element_by_id("name").send_keys(self.wrongUserAccount[1]['username'])
    #     self.driver.find_element_by_id("password").send_keys(Keys.SPACE)
    #     self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[5]/div/div/span/button').click()
    #     sleep(2)
    #     logInfo = '错误密码_空格'
    #     self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
    #     alert_info = self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[3]/div/div/div')
    #     self.assertIn('输入密码', alert_info.text)
    #
    # def test_login_pwd_null(self):
    #     '''密码不正确-空'''
    #     self.login(self.wrongUserAccount[2]['username'], self.wrongUserAccount[2]['password'])
    #     sleep(2)
    #     logInfo = '错误密码_空'
    #     self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
    #     alert_info = self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[3]/div/div/div')
    #     self.assertIn('输入密码', alert_info.text)
    #
    # def test_login_username_unregistered(self):
    #     '''用户名不正确'''
    #     self.login(self.wrongUserAccount[3]['username'], self.wrongUserAccount[3]['password'])
    #     sleep(2)
    #     logInfo = '错误账户_未注册'
    #     self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
    #     alert_info = self.driver.find_element_by_xpath('/html/body/div[2]/span/div/div/div/span')
    #     self.assertIn('用户信息有误', alert_info.text)
    #
    # def test_login_username_space(self):
    #     '''用户名不正确-空格'''
    #     self.driver.find_element_by_id("name").send_keys(Keys.SPACE)
    #     self.driver.find_element_by_id("password").send_keys(self.wrongUserAccount[4]['password'])
    #     self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[5]/div/div/span/button').click()
    #     sleep(2)
    #     logInfo = '错误账户_空格'
    #     self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
    #     alert_info = self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[2]/div/div/div')
    #     self.assertIn('输入账户名', alert_info.text)
    #
    # def test_login_username_null(self):
    #     '''用户名不正确-空'''
    #     self.login(self.wrongUserAccount[5]['username'], self.wrongUserAccount[5]['password'])
    #     sleep(2)
    #     logInfo = '错误账户_空'
    #     self.driver.get_screenshot_as_file(self.errorScreenCapPath + "\\error_login_" + logInfo + ".png")
    #     alert_info = self.driver.find_element_by_xpath(
    #         '//*[@id="popContainer"]/div/div[1]/div/div[2]/form/div[2]/div/div/div')
    #     self.assertIn('输入账户名', alert_info.text)

    def tearDown(self):
        print('当前用例执行完毕！')
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        print("----智能床垫后台登录模块测试结束！")


if __name__ == '__main__':
    unittest.main()
