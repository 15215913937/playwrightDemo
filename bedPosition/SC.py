# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/23 23:16

class SC():
    def __init__(self, driver):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
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

        # self.driver.implicitly_wait(10)

    def open_page(self, url):
        self.driver.get(url)

    def find_element_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath)

    def quit(self):
        self.driver.quit()
