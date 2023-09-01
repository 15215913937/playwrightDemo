# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/31 14:24
import os.path

from common.Excels import NewExcel, OldExcel


def get_reader(srcfile='') -> NewExcel.Reader:
    reader = None
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
        return reader

    if srcfile.endswith('.xlsx'):
        reader = NewExcel.Reader()
        reader.open_excel(srcfile)
        return reader

    # if srcfile.endswith('.xls'):
    #     reader = OldExcel.Reader()
    #     reader.open_excel(srcfile)
    #     return reader


# 调试
if __name__ == '__main__':
    reader = get_reader('../lib/cases/pc端测试用例.xlsx')
    sheetname = reader.get_sheets()
    print(sheetname)
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        lines = reader.readline()
        print(lines)
        break
