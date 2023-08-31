# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/31 15:55
import logging
import os.path
import yaml


class Logger:
    def __init__(self, path: str = './'):
        if not os.path.isfile(path + 'lib/conf.yml'):
            path = '../'

        with open(file=path + 'lib/conf.yml', mode='r', encoding='utf-8') as file:
            logging_yml = yaml.safe_load(stream=file).get('logger')
            logging_yml['filename'] = path + logging_yml.get('filename')
            logging.basicConfig(**logging_yml)

        # 根据根记录器，配置信息从yaml文件中获取
        self.logger = logging.getLogger()
        # 创建输出到控制台
        console = logging.StreamHandler()
        # 设置日志等级
        console.setLevel(logging_yml['level'])
        # 设置日志格式
        console.setFormatter(logging.Formatter(logging_yml['format']))
        # 添加到logger输出
        self.logger.addHandler(console)

    def debug(self, msg: str = ''):
        self.logger.debug(msg)

    def info(self, msg: str = ''):
        self.logger.info(msg)

    def warning(self, msg: str = ''):
        self.logger.warning(msg)

    def error(self, msg: str = ''):
        self.logger.error(msg)

    def exception(self, e):
        self.logger.exception(e)


logger = Logger()
