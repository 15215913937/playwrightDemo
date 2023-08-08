import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def get_input():
    """获取输入参数"""
    input_file = Path(input("输入Excel文件:"))
    output_file = Path(input("输出Excel文件:"))
    area_param = float(input("输入面积转换参数:"))
    count_param = int(input("设置自定义面积的参数个数:"))

    return input_file, output_file, area_param, count_param


def read_data(input_file):
    """读取Excel数据"""
    try:
        # df = pd.read_excel(input_file, usecols="A")  # 只读取第一列
        df = pd.read_excel(input_file)  # 只读取第一列
        return df
    except Exception as e:
        logger.exception("读取Excel失败")
        raise e


def process_data(df, area_param, count_param):
    """处理数据"""
    df["count"] = df.groupby(df.columns[0]).transform("count")
    df["area"] = df[df.columns[0]] * area_param
    df["area"] = df.groupby(df.columns[0])["area"].transform("sum")
    df["id"] = range(len(df))
    df["group"] = df["id"] // count_param
    return df


def write_data(df, output_file):
    """写入Excel"""
    try:
        df.to_excel(output_file, index=False)
    except Exception as e:
        logger.exception("写入Excel失败")
        raise e


def main():
    """主函数"""
    input_file, output_file, area_param, count_param = get_input()
    df = read_data(input_file)
    df = process_data(df, area_param, count_param)
    write_data(df, output_file)

    print("转换完成!")


if __name__ == '__main__':
    main()