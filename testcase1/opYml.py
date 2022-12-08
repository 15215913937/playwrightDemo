# coding = utf-8
# Author: Shenbq
# Date: 2022/9/6 18:04
import os

import yaml


def getYml(yml_file):
    # 读取文件操作---从磁盘读取到内存
    fo = open(yml_file, 'r', encoding='utf-8')
    # 使用yaml方法获取数据
    res = yaml.load(fo, Loader=yaml.FullLoader)
    return res


def getCommonYml():
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    commonPath = os.path.join(curPath, "utils\\common.yml")
    # open方法打开直接读出来
    return getYml(commonPath)

def getUserYml():
    # 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    commonPath = os.path.join(curPath, "utils\\user.yml")
    # open方法打开直接读出来
    return getYml(commonPath)


if __name__ == '__main__':
    # list = getYml('D:\\pythonwork\\CommonScripts\\testcase1\\utils\\user.yml')
    # user = list.get('CorrectUserAccount')
    # print(user['username'])
    print(getUserYml())
    # a = 'admin'
    # try:
    #     assert a == username
    #     print("成功")
    # except Exception:
    #     print("失败")
