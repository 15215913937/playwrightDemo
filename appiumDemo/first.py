# coding = utf-8
# Author: Shenbq
# Date: 2022/11/25 14:03
# 1 设置终端参数
desired_caps = {
    "platformName": "Android", # 操作平台
    # adb shell getprop ro.build.version.release
    "platformVersion": "10", # 操作平台版本
    # adb devices
    "deviceName": "Q5S0219430015769", # 设备名称
    # adb shell dumpsys window | findstr mCurrentFocus 或
    # aapt dump badging C:\Users\sqn\Desktop\bed_user_test_1.9.8.apk | findstr launchable-activity
    "appPackage": "uni.UNI02D9911", # 应用名称
    "appActivity":"io.dcloud.PandoraEntry", # app启动项名称
    "noReset": True # 是否重置
}

from appium import webdriver
# 2 appinum server 启动
# 3 发送指令到appinum server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)