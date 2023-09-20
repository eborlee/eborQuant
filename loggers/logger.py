# -*- encoding: utf-8 -*-
'''
@File    :   logger.py

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/26 15:18    eborlee      1.0         None
'''

import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from observers.observer import Observer

class Logger(Observer):
    def __init__(self, log_file):
        handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=10, encoding='utf8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def update(self, message):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{message}"
        self.logger.info(log_message)

