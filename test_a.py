# coding = utf-8
# Author: Shenbq
# Date: 2022/12/2 13:27
import pytest
from selenium import webdriver
from time import sleep

def test_baidu_search_01():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('博客园 韩志超')
    driver.find_element_by_id('su').click()
    sleep(1)
    assert '韩志超' in driver.title, '标题不包含韩志超'  # 自定义失败消息
    driver.quit()

if __name__ == '__main__':
    pytest.main([__file__])