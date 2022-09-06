# coding = utf-8
# Author: Shenbq
# Date: 2022/8/11 13:22
'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''
import time
import unittest
from selenium import webdriver
from time import sleep


class LoginCase(unittest.TestCase):

    def setUp(self):
        # 指定浏览器
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        # 指定打开页面地址
        self.driver.get('http://bed.test.cnzxa.cn/#/login')
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/div/div/span/span/input").send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/form/div[3]/div/div/span/span/input").send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/form/div[5]/div/div/span/button").click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('admin', 'admin')  # 正确用户名和密码
        sleep(3)
        username = self.driver.find_element_by_class_name('name')
        self.assertTrue('admin' in username.text)  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里\
        # 获取格式化的当前时间
        ran_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.driver.get_screenshot_as_file("d:/testplace/success_login_" + ran_str + ".png")  # 截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确，密码不正确'''
        self.login('admin', 'aa')
        sleep(2)
        alert_info = self.driver.switch_to.alert()
        print(alert_info.text)

    # def test_login_pwd_error(self):
    #     '''用户名正确、密码不正确'''
    #     self.login('kemi_xxx', 'kemi')  #正确用户名，错误密码
    #     sleep(2)
    #     error_message = self.driver.find_element_by_id('tip_btn').text
    #     self.assertIn('用户名或密码错误', error_message)  #用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
    #     self.driver.get_screenshot_as_file("D:\cnblogtest\\login_pwd_error.jpg")
    #
    # def test_login_pwd_null(self):
    #     '''用户名正确、密码为空'''
    #     self.login('kemi_xxx', '')  #密码为空
    #     error_message = self.driver.find_element_by_id('tip_input2').text
    #     self.assertEqual(error_message,'请输入密码')  #用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
    #     self.driver.get_screenshot_as_file("D:\cnblogtest\\login_pwd_null.jpg")
    #
    # def test_login_user_error(self):
    #     '''用户名错误、密码正确'''
    #     self.login('kemixing', 'kemi_xxx')  #密码正确，用户名错误
    #     sleep(2)
    #     error_message = self.driver.find_element_by_id('tip_btn').text
    #     self.assertIn('该用户不存在', error_message)  #用assertIn(a,b)方法来断言 a in b
    #     self.driver.get_screenshot_as_file("D:\cnblogtest\\login_user_error.jpg")
    #
    # def test_login_user_null(self):
    #     '''用户名为空、密码正确'''
    #     self.login('', 'kemi_xxx')  #用户名为空，密码正确
    #     error_message = self.driver.find_element_by_id('tip_input1').text
    #     self.assertEqual(error_message,'请输入登录用户名')  #用assertEqual(a,b)方法来断言  a == b
    #     self.driver.get_screenshot_as_file("D:\cnblogtest\\login_user_null.jpg")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
