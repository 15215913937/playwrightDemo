# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/15 17:57
import logging
class LoginConfig:
    @staticmethod
    def LoginFormat(info):
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

        logging.info(info)
