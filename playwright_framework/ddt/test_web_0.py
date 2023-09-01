# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/9/1 10:19
import time

import pytest

from ddt.excel_ddt import ddt
import allure

@allure.feature('#' + str(ddt.feature_idx) + '' + ddt.feature)
class Test_Web:
    @allure.step
    def run_step(self,func,params):
        if params:
            return func(*params)
        else:
            return func()

    @allure.story('#' + str(ddt.story_idx) + '' + ddt.story)
    @pytest.mark.parametrize('cases',ddt.cases)
    def test_case(self,cases):
        '''测试用例'''
        time.sleep(1)
        allure.dynamic.title(cases[0][1])
        cases=cases[1:]
        try:
            for case in cases:
                func = getattr(ddt.web,case[3])
                # 参数处理
                params = cases[4:]
                # 截取非空参数
                params = params[:params.index('')]
                with allure.step(case[2]):
                    self.run_step(func,params)
            time.sleep(0.3)
            # 成功后截图
            allure.attach(ddt.web.screenshot(),'成功截图',allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(ddt.web.screenshot(), '失败截图', allure.attachment_type.PNG)