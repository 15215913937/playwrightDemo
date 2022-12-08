# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/1 17:08

import time

import pytest

from pages.login import Login
from utilities.data_helper import read_data_from_excel, read_data_from_json_yaml


@pytest.mark.login
class TestLogin:

    @pytest.mark.parametrize('username,password,expect_string', read_data_from_json_yaml('../configs/data/login.yml'))
    def test_login(self, username, password, expect_string):
        login = Login('Chrome')
        assert_result = login.login(username, password)
        assert (expect_string in assert_result) is True


if __name__ == "__main__":
    pytest.main(["-m", "login", "-s", "-v"])
