# coding = utf-8
# Author: Shenbq
# Date: 2022/1/13 14:50
import unittest

import pytest
import requests
import yaml


def read_yaml():
    with open("select_flag.yml", encoding="utf-8") as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
        return result


class TestApi:
    access_token = ""

    def test_01_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        res = requests.get(url, params)
        TestApi.access_token = res.json()['access_token']
        print("token值是=\"" + TestApi.access_token + "\"")

    @pytest.mark.parametrize("caseinfo", read_yaml())
    def test_02_select_tag(self, caseinfo):
        print(caseinfo)
        # url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        # params = {
        #     "access_token": TestApi.access_token
        # }
        # res = requests.get(url, params)
        # print(res.json())

    def test_03_get_new(self):
        url = "https://api.apiopen.top/getWangYiNews"
        data = {
            "pages": "1",
            "count": "5"
        }
        res = requests.get(url, data)
        print(res.json())


if __name__ == '__main__':
    pytest.main()
