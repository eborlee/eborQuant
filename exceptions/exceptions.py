# -*- encoding: utf-8 -*-
'''
@File    :   exceptions.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/20 20:53    eborlee      1.0         None
'''

class StrategyException(Exception):
    """基本策略异常"""
    def __init__(self, message=None):
        if message is None:
            message = "An error occurred in the strategy execution"
        super().__init__(message)


class DatabaseException(StrategyException):
    """数据库相关异常"""
    def __init__(self, message=None):
        if message is None:
            message = "An error occurred while interacting with the database"
        super().__init__(message)


class TradingException(StrategyException):
    """交易操作异常"""
    def __init__(self, message=None):
        if message is None:
            message = "An error occurred during the trading process"
        super().__init__(message)

# 可以根据需要继续添加更多具体的异常类

