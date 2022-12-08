# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/2 16:22
import yaml


class YmlHelper:
    @staticmethod
    def read_yml(yml_file_path):
        with open(yml_file_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
