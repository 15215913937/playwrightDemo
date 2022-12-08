# coding = utf-8
# Author: Shenbq
# Date: 2022/11/29 17:42
import HTMLTestRunner
import unittest

if __name__ == "__main__":
    # 测试用例保存的目录
    case_dirs = r"D:\pythonwork\CommonScripts\testcase1"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_dirs, "test_*.py")
    # 运行测试用例同时保存测试报告
    test_report_path = r"D:\pythonwork\CommonScripts\testcase1\reports\report.html"
    with open(test_report_path, "w", encoding="utf-8") as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="智能床垫后台登录功能测试")
        runner.run(discover)
