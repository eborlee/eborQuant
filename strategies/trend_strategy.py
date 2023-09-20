# -*- encoding: utf-8 -*-
'''
@File    :   trend_strategy.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/27 15:22    eborlee      1.0         None
'''

from collections import deque
import importlib
import time

from strategies.base_strategy import BaseStrategy


class TrendStrategy(BaseStrategy):
    def __init__(self, database_manager, trade_engine, config):
        super().__init__(database_manager, trade_engine, config)
        self.time_frame = config.get('time_frame', '1m')  # 交易时间级别
        self.asset = config.get('asset', 'BTC')  # 交易标的
        self.close_prices = deque(maxlen=1000)  # 存储最近1000个close价格
        self.indicator_func = self.load_indicator_func(config.get('indicator', 'sma'))  # 从配置加载技术指标函数

    def load_indicator_func(self, indicator_name):
        indicators_module = importlib.import_module('indicators')
        return getattr(indicators_module, indicator_name)

    def update_close_prices(self, new_close_price):
        self.close_prices.append(new_close_price)

    def update_indicator(self):
        if len(self.close_prices) == 1000:
            self.indicator_value = self.indicator_func(self.close_prices)

    def main_loop(self):
        while True:
            new_close_price = self.database_manager.get_latest_close_price(self.time_frame, self.asset)
            self.update_close_prices(new_close_price)
            self.update_indicator()
            self.run()
            time.sleep(self.config.get('loop_interval', 60))

    def run(self):
        # 在这里添加策略逻辑
        signal = self.generate_signal()
        if signal:
            self.place_order(signal)

    def generate_signal(self):
        # 在这里添加策略逻辑和信号触发规则，可能会用到self.indicator_value
        pass
