# -*- encoding: utf-8 -*-
'''
@File    :   strategy1.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 11:54    eborlee      1.0         None
'''
from strategies.base_strategy import BaseStrategy


class Strategy(BaseStrategy):

    name = "debug策略脚本"

    def run(self):
        while True:
            pass