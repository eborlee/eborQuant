# -*- encoding: utf-8 -*-
'''
@File    :   strategy_manager.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 11:29    eborlee      1.0         None
'''
import pickle
from datetime import datetime
from multiprocessing import Process
from core.trade_engine import TradeEngine
from database.DatabaseManager import DatabaseManager
from notification.telebot import TelegramNotifier
import time

from strategies.strategy1 import Strategy
from utils import MessageType


def run_strategy():
    # 以下内容根据实际需求调整
    # trade_engine = TradeEngine()
    # database_manager = DatabaseManager()
    # # notifier = TelegramNotifier(self.bot_token, self.chat_id)
    #
    # # 注册观察者
    # trade_engine.register_observer(database_manager)
    # # trade_engine.register_observer(notifier)
    #
    # strategy = Strategy(database_manager, trade_engine,{})
    # trade_engine.register_observer(strategy)
    # strategy.execute()
    pass

class StrategyManager:
    def __init__(self, config, logger):
        self.config = config
        self.db_param = config.get_db_params()
        self.strategies = {} # 存储策略和进程的映射
        self.processes = {} # 存储策略的进程
        self.bot_token = config.get_notifications_param('telegram')['bot_token']
        self.chat_id = config.get_notifications_param('telegram')['chat_id']
        self.monitoring_process = Process(target=self._monitor_processes)  # 使用Process而不是Thread
        self.monitoring_process.start()  # 启动监控进程
        self.notifier = TelegramNotifier(self.bot_token, self.chat_id)

        self.logger = logger

        self.database_manager = DatabaseManager(self.db_param)
        self.database_manager.register_observer(self.notifier)
        self.database_manager.register_observer(logger)

    @classmethod
    def _run_strategy(cls, strategy_class, db_config, strategy_config, bot_token, chat_id):
        # 以下内容根据实际需求调整
        # trade_engine = TradeEngine()
        database_manager = DatabaseManager(db_config)
        notifier = TelegramNotifier(bot_token,chat_id)

        notifier.update(f"策略[{strategy_class.name}]已启动！")
        #
        # # 注册观察者
        # trade_engine.register_observer(database_manager)
        # # trade_engine.register_observer(notifier)
        #
        # strategy = strategy_class(database_manager, trade_engine,config)
        # trade_engine.register_observer(strategy)
        # strategy.execute()
        pass





    def _monitor_processes(self):

        notifier = TelegramNotifier(self.bot_token, self.chat_id)

        while True:
            for strategy_name, process in self.processes.items():
                if process and not process.is_alive():
                    notifier.update(f"Strategy {strategy_name} has stopped. Restarting...")
                    self.start_strategy(strategy_name)
            time.sleep(60)  # 每60秒检查一次

    def register_strategy(self, strategy_class, strategy_id, config):
        self.strategies[strategy_id] = (strategy_class,  config)
        strategy_data = {
            'strategy_id': strategy_id,
            'strategy_name': strategy_class.name,
            'strategy_class': strategy_class.__name__,
            'status': 0  # 或者从config或其他地方获取
        }
        self.database_manager.add_strategy(strategy_data)
        self.notifier.update(f"{strategy_class.name} 已注册")
        self.logger.update("策略已注册")

    def start_strategy(self, strategy_id):
        # strategy_name = 'strategy' + strategy_name
        strategy_class, config = self.strategies[strategy_id]
        print(type(config))
        # pickle.dumps(strategy_class)
        # pickle.dumps(config)
        print(strategy_class, config)
        process = Process(target=StrategyManager._run_strategy,
                          args=(strategy_class, self.db_param, config, self.bot_token, self.chat_id))
        process.start()
        self.processes[strategy_id] = process
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.database_manager.update_strategy(strategy_id,
                                              current_time,
                                              status=1)
        self.logger.update("策略已启动")

    def pause_strategy(self, strategy_name):
        process = self.processes[strategy_name]
        process.terminate()
        self.processes[strategy_name] = None

    def resume_strategy(self, strategy_name):
        strategy_class, config = self.strategies[strategy_name]
        self.start_strategy(strategy_name, config)

    def stop_all_strategies(self):
        for process in self.processes.values():
            if process is not None:
                process.terminate()

    # 扩展部分，可根据手机端传来的命令回复相应信息
    def handle_remote_command(self, command):
        if command == "check_status":
            status_report = {name: "Running" if process and process.is_alive() else "Stopped"
                            for name, process in self.processes.items()}
            return status_report

    def get_active_strategies(self):
        return [name for name, process in self.processes.items()
                if process and process.is_alive()]

    def get_loaded_strategies(self):
        return [name for name, process in self.strategies.items()]