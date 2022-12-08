# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/2 15:01
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self, driver):
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")

        if str(driver).capitalize() == "Chrome":
            self.driver = webdriver.Chrome(options=options)
        elif str(driver).capitalize() == "Firefox":
            self.driver = webdriver.Firefox()
        elif str(driver).capitalize() == "Edge":
            self.driver = webdriver.Edge()
        elif str(driver).capitalize() == "Safari":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(10)

    def open_page(self, url):

        self.driver.get(url)
