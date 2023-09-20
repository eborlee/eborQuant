# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pickle
from queue import Queue
import telebot
from configs import ConfigLoader
from core.cerebro import Cerebro
from notification import CommandProcessor
from strategies.strategy1 import Strategy as Strategy1
from telegram.ext import Updater, CommandHandler, Dispatcher


# from strategy_manager import StrategyManager
# from trade_engine import TradeEngine
# from database_manager import DatabaseManager
# from plugin_manager import PluginManager
# from your_strategy import YourStrategy  # 假设你有一个策略类定义为YourStrategy


def main():
    config = ConfigLoader("./configs/sys_config.yaml")

    bot_token = config.get_notifications_param('telegram')['bot_token']
    chatid = config.get_notifications_param('telegram')['chat_id']

    # 初始化交易引擎、数据库管理器和插件管理器
    # plugin_manager = PluginManager()

    # 初始化策略管理器
    cerebro = Cerebro(config)
    cerebro.add_strategy('001', Strategy1, config)

    # pickle.dumps(Strategy1)
    # pickle.dumps(config)
    cerebro.start_strategy('001')
    # 用户命令界面
    # while True:
    #     command = input("Enter command (add/start/stop/plugin/exit): ")
    #
    #     if command == "add":
    #         strategy_id = input("Enter strategy ID (e.g., 001): ")
    #         # 此处可以进一步选择策略类型或直接使用YourStrategy
    #         cerebro.add_strategy(strategy_id, Strategy1)
    #
    #     elif command == "start":
    #         strategy_id = input("Enter strategy ID to start: ")
    #         cerebro.start_strategy(strategy_id)
    #
    #     elif command == "stop":
    #         strategy_id = input("Enter strategy ID to stop: ")
    #         cerebro.stop_strategy(strategy_id)
    #
    #     elif command == "plugin":
    #         plugin_command = input("Enter plugin command (start/stop): ")
    #         plugin_name = input("Enter plugin name: ")
    #         if plugin_command == "start":
    #             plugin_manager.start_plugin(plugin_name)
    #         elif plugin_command == "stop":
    #             plugin_manager.stop_plugin(plugin_name)
    #
    #     elif command == "exit":
    #         cerebro.strategy_manager.stop_all_strategies()
    #         break




    command_processor = CommandProcessor(cerebro.strategy_manager,
                                         bot_token, chatid)
    command_processor.run()





if __name__ == "__main__":
    main()
