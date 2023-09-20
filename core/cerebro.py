# -*- encoding: utf-8 -*-
'''
@File    :   cerebro.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 11:51    eborlee      1.0         None
'''
from database import DatabaseManager
from loggers.logger import Logger
from .strategy_manager import StrategyManager
# from strategies.my_strategy import MyStrategy
from pathlib import Path



class Cerebro:
    '''
    Cerebro类 - 作为交易系统的主要入口点，负责协调其他组件，
    如数据库管理器、策略管理器等，并且负责添加和配置交易策略。
    '''

    def __init__(self,config):
        # 获取当前脚本的路径
        current_path = Path(__file__).resolve()

        # 获取当前脚本的父目录
        parent_path = current_path.parent.parent

        # 创建日志文件的路径
        log_file_path = parent_path / 'app.log'
        print(log_file_path)

        self.strategies = {}  # 使用字典存储策略编号和类的映射
        self.config = config
        self.logger = Logger(log_file_path)
        self.bot_token = config.get_notifications_param('telegram')['bot_token']
        self.chatid = config.get_notifications_param('telegram')['chat_id']
        self.strategy_manager = StrategyManager(config, self.logger)
        # self.database_manager = DatabaseManager()

    def add_strategy(self, strategy_id, strategy_class, config, *args, **kwargs):
        self.strategies[strategy_id] = (strategy_class, config, args, kwargs)
        # strategy_name = "strategy" + str(strategy_id)
        self.strategy_manager.register_strategy(strategy_class, strategy_id, config)

    def start_strategy(self, strategy_id):
        strategy_class, config, args, kwargs = self.strategies[strategy_id]
        self.strategy_manager.start_strategy(strategy_id)

    def stop_strategy(self, strategy_id):
        strategy_name = self.strategies[strategy_id][0].__name__
        self.strategy_manager.pause_strategy(strategy_name)