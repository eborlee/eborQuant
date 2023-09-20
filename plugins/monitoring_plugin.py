# -*- encoding: utf-8 -*-
'''
@File    :   monitoring_plugin.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 19:32    eborlee      1.0         None
'''
# monitoring_plugin.py
from base_plugin import PluginBase


class MonitoringPlugin(PluginBase):
    def __init__(self, strategy, trade_engine, threshold):
        super().__init__()
        self.strategy = strategy
        self.trade_engine = trade_engine
        self.threshold = threshold

    def monitor_market(self, market_data):
        # 监控市场数据和策略的持仓情况
        positions = self.strategy.get_positions()
        for symbol, position in positions.items():
            if market_data[symbol].change_percentage > self.threshold:
                # 暴涨暴跌，触发平仓
                self.trade_engine.close_position(symbol)
                # 通知所有观察者（子策略）平仓事件
                self.notify_observers('close_position', {'symbol': symbol})

    def execute(self):
        # 在这里添加获取市场数据和持仓的代码，并调用monitor_market进行监控
        pass
