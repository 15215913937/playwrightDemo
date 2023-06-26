# coding = utf-8
# Author: Shenbq
# Date: 2022/10/27 14:10
import time
import pymysql
from selenium import webdriver
from PIL import ImageGrab


def screenCap(flag, position_recognition, savePath):
    config = {
        'host': 'mysql.test.cnzxa.cn',
        'port': 23306,
        'user': 'user',
        'passwd': 'Comfab.088',
        'db': 'test',
        'charset': 'utf8',
    }

    conn = pymysql.connect(**config)
    # 生成游标对象
    cur = conn.cursor()

    selectSql = "select * from bed_pressure where flag=%s and position_recognition=%s" % (flag, position_recognition)

    cur.execute(selectSql)
    conn.commit()
    data = cur.fetchall()

    driver = webdriver.Chrome()
    # 打开网址
    driver.get("http://bedimg.test.cnzxa.cn/#/")
    driver.maximize_window()
    # 元素定位
    input = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-input/div/input')
    add = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]')
    clear = driver.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]')
    # clear.click()
    # input.clear()
    # 截图区域设置
    bbox = (0, 180, 400, 900)
    start_time = time.time()
    for datum in data:
        clear.click()
        input.clear()
        val = datum[1]
        input.send_keys(val)
        add.click()
        time.sleep(1)
        im = ImageGrab.grab(bbox)
        # 截图存放位置
        im.save((savePath + "\\%s.png") % (datum[0]))
        # im.save("D:\\workspace\\bed_position\\screencap\\0\\%s.png" % (datum[0]))
    driver.quit()
    end_time = time.time()
    duration = end_time - start_time
    return duration


if __name__ == '__main__':
    flag = '23032301'
    position_recognition = 0
    savePath = 'D:\\workspace\\bed_position\\screencap\\0'
    duration = screenCap(flag, position_recognition, savePath)
    print("执行%d秒" % duration)
