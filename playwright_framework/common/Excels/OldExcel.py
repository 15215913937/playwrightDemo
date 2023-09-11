# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/31 14:29
import os

import xlrd


class Reader:
    '''
    pip install openpyxl
    '''

    def __init__(self):
        self.workbook = None
        self.sheet = None
        self.rows = 0
        self.r = 0  # 当前读取到的行数

    def open_excel(self, srcfile):
        if not os.path.isfile(srcfile):
            print("%s not exist!" % (srcfile))
            return

        xlrd.Book.encoding = 'utf-8'
        # 读取excel内容缓存到workbook中
        self.workbook = xlrd.open_workbook(filename=srcfile)
        self.sheet = self.workbook.sheet_by_index(0)
        self.rows = self.sheet.nrows
        self.r = 0
        return

    def get_sheets(self):
        sheets = self.workbook.sheet_names()
        return sheets

    # 切换sheet页面
    def set_sheet(self, name):
        self.sheet = self.workbook.sheet_by_name(name)
        self.rows = self.sheet.nrows
        self.r = 0
        return

    def readline(self):
        lines = []
        # 不是最后一行，则往下读取一行
        while self.r < self.rows:
            row1 = None
            # 读取第r行内容
            row = self.sheet.row_values(self.r)
            self.r = self.r + 1
            i = 0
            row1 = row
            for strs in row:
                row1[i] = str(strs)
                i = i + 1
            lines.append(row1)
        return lines


class Writer:
    def __init__(self):
        self.workbook = None
        self.wb = None
        self.sheet = None
        self.df = None
        self.row = 0
        self.col = 0

    def copy_open(self, srcfile, dstfile):
        if not os.path.isfile(srcfile):
            print(srcfile + " not exist!")
            return

        if os.path.isfile(dstfile):
            print(dstfile + " file already exist!")