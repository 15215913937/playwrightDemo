# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/2 16:20
import logging
import os.path
import time

from selenium.webdriver.common.by import By
from utilities.yml_helper import YmlHelper
from pages.base_page import BasePage
from utilities.loginConfig import LoginConfig


class Login(BasePage):
    element_locator_yml = os.path.abspath(os.path.join(os.path.dirname(__file__), '../configs/ymls/login.yml'))
    element = YmlHelper.read_yml(element_locator_yml)
    username_input_box = (By.ID, element['USERNAME_LOCATOR'])
    pwd_input_box = (By.ID, element['PASSWORD_LOCATOR'])
    login_button = (By.XPATH, element['LOGIN_BUTTON_LOCATOR'])
    assert_object = (By.ID, element['SEARCH_KEY_LOCATOR'])
    base_url = element['BASE_URL']
    # LoginConfig.LoginFormat(username_input_box)
    # LoginConfig.LoginFormat(pwd_input_box)
    # LoginConfig.LoginFormat(login_button)
    # LoginConfig.LoginFormat(assert_object)
    # LoginConfig.LoginFormat(base_url)

    def __init__(self, driver):
        # 构造函数继承自父类BasePage
        super().__init__(driver)

    def login(self, username, password):
        driver = self.driver
        self.open_page(self.base_url)
        # * 代表可变位置参数
        # 清空输入框内容
        # driver.find_element(*self.username_input_box).clear()
        # driver.find_element(*self.pwd_input_box).clear()
        # 输入内容
        driver.find_element(*self.username_input_box).send_keys(username)
        LoginConfig.LoginFormat(self.username_input_box)
        driver.find_element(*self.pwd_input_box).send_keys(password)
        driver.find_element(*self.login_button).click()
        time.sleep(2)
        assert_object = driver.find_element(*self.assert_object).text
        return assert_object

if __name__ == '__main__':
    login = Login('chrome')
    login.login('15215913937','123')