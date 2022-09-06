# coding = utf-8
# Author: Shenbq
# Date: 2021/12/15 16:50
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

s = requests.Session()
s.headers.update(headers)
# s.auth = ('superuser', '123')
s.get('https://www.kuaipan.cn/account_login.htm')

_URL = 'http://www.kuaipan.cn/index.php'
s.post(_URL, params={'ac': 'account', 'op': 'login'},
       data={'username': '****@foxmail.com', 'userpwd': '********', 'isajax': 'yes'})
r = s.get(_URL, params={'ac': 'zone', 'op': 'taskdetail'})
print(r.json())

# driver = webdriver.Chrome()
# driver.get(url)
# driver.implicitly_wait(3)
# a = EC.title_contains('百度一下')(driver)
# print(a)
# input_search = (By.ID,"kw")
# try:
#     ele = WebDriverWait(driver,20,1).until(EC.presence_of_element_located(input_search))
# except:
#     print("该元素不存在")
# else:
#     ele.send_keys("sqn")
# driver.find_element(By.ID, "kw").send_keys("北京")
# driver.find_element(By.ID, "su").click()
# # 定位元素
# ele = driver.find_element(By.XPATH, '//*[@id="1"]/div/div/h3/a')
# # 显示等待，实例化对象
# wait = WebDriverWait(driver, 20, 0.5)
# # 调用until()方法，判断元素是否出现
# wait.until(lambda x: ele.is_displayed())
# ele.click()
# time.sleep(2)
# driver.quit()

# driver = webdriver.Chrome()
# driver.get("http://video.baidu.com/")
# driver.implicitly_wait(3)
# driver.maximize_window()
# current_handle1 = driver.current_window_handle
# print(current_handle1)
# driver.find_element_by_link_text('输赢').click()
# handles = driver.window_handles
# print(handles)
# driver.switch_to.window(handles[1])
# current_handle2 = driver.current_window_handle
# current_title = driver.title
# print(current_title)
# time.sleep(3)
# print(current_handle1,current_handle2)
# driver.switch_to.window(handles[0])
# current_handle3 = driver.current_window_handle
# print(driver.title)
