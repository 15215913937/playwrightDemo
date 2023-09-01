# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/31 13:56
import os

from ddt.excel_ddt import ddt

if __name__ == '__main__':
    os.system('rm -rf result')
    os.system('rm -rf report')

    ddt.run_web_case('./lib/cases/pc端测试用例.xlsx')
    os.system('allure generate result -o report --clean')