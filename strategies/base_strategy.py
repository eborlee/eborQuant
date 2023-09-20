# -*- encoding: utf-8 -*-
'''
@File    :   base_strategy.py  

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 11:43    eborlee      1.0         None
'''
import logging

from exceptions.exceptions import StrategyException
from observers.observer import Observer


class BaseStrategy(Observer):
    def __init__(self, database_manager, trade_engine, config):
        self.database_manager = database_manager
        self.trade_engine = trade_engine
        self.config = config
        self.strategy_state = None  # 这可以用来记录策略的状态，例如初始化、运行等
        self.initialize()

    def initialize(self):
        # 在这里放置一些策略的初始化代码，例如加载配置文件、设置初始状态等
        pass

    def execute(self, *args, **kwargs):
        """封装策略执行，并处理可能的异常"""
        try:
            self.run(*args, **kwargs)
        except StrategyException as e:
            logging.error(str(e))
            self.handle_error(e)
        except Exception as e:
            logging.error(f"Unhandled error in strategy: {str(e)}")
            self.handle_error(e)

    def run(self, *args, **kwargs):
        """
        子类需要实现这个方法来定义具体的策略逻辑
        例如：
            1. 从数据库加载数据
            2. 执行交易逻辑
            3. 更新数据库状态
        """
        raise NotImplementedError("Subclasses must implement the run method.")

    def handle_error(self, exception):
        """
        在这里处理错误，例如更新数据库状态等。
        这个方法也可以由子类覆盖以提供具体的错误处理逻辑。
        """
        # 例子：可以更新数据库中该策略的状态为“失败”，记录错误信息等
        pass

    def place_order(self, order_data):
        # 执行下单操作，并自动将订单数据发送给数据库模块
        self.database_manager.process_order(order_data)

    def log(self, message):
        # 可以添加一些日志功能，记录策略的重要信息
        print(f"Strategy log: {message}")

    def on_signal(self, signal_data):
        # 这是一个可选的方法，可以用来处理从市场、其他策略或系统中收到的信号
        pass

    # 可以添加其他通用方法和属性
