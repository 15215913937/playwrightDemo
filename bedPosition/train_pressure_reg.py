# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/23 22:53
from time import sleep, time
from PIL import ImageGrab
from DataBases import DataBases as db
from selenium import webdriver


def screenCap(sc_url, position_real, savePath):
    config = {
        'host': 'mysql.test.cnzxa.cn',
        'port': 23306,
        'user': 'user',
        'passwd': 'Comfab.088',
        'db': 'test',
        'charset': 'utf8',
    }

    # 实例化数据库对象sor
    sor = db(host=config['host'], port=config['port'], user=config['user'], password=config['passwd'],
             database=config['db'])
    sql1 = 'select * from train_pressure where position_real = %s' % position_real

    res = sor.get_all(sql1)

    driver = webdriver.Chrome()
    # 打开网址
    driver.get(sc_url)
    driver.maximize_window()
    # 元素定位
    input = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-input/div/input')
    add = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]')
    clear = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]')

    bbox = (0, 180, 400, 900)

    for re in res:
        clear.click()
        input.clear()
        val = re[1]
        input.send_keys(val)
        add.click()
        sleep(1)
        im = ImageGrab.grab(bbox)
        # 截图存放位置
        im.save((savePath + "\\%s\\%s.png") % (position_real, re[0]))
        sql2 = "update train_pressure set flag = 1 where id = %s" % re[0]
        sor.update(sql2)
    driver.quit()


if __name__ == '__main__':
    sc_url = 'http://bedimg.test.cnzxa.cn/#/'
    savePath = 'D:\\workspace\\train_pressure'
    position_real = 1
    start_time = time()
    screenCap(sc_url, position_real, savePath)
    position_real = 3
    screenCap(sc_url, position_real, savePath)
    end_time = time()
    duration = end_time - start_time
    print("耗时 %s 秒" % duration)
