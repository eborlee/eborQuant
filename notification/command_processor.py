# -*- encoding: utf-8 -*-
'''
@File    :   command_processor.py
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/22 15:34    eborlee      1.0         None
'''
import telebot

from .commands import TelebotCommands


class CommandProcessor:
    def __init__(self, strategy_manager, bot_token, chat_id):
        self.chat_id = chat_id
        self.strategy_manager = strategy_manager
        print(self.chat_id)

        self.bot = telebot.TeleBot(bot_token)

        self.bot.message_handler(commands=['start'])(self.send_welcome)
        self.bot.message_handler(commands=['hi'])(self.send_hi)
        self.bot.message_handler(commands=['help'])(self.handle_help)
        self.bot.message_handler(commands=['running'])(self.show_active_strategies)
        self.bot.message_handler(commands=['loaded'])(self.show_loaded_strategies)
        # self.bot.message_handler(commands=['active_strategies'])(self.show_active_strategies)

        self.bot.send_message(chat_id, TelebotCommands.INIT_WORDS)

    def send_welcome(self, message):
        self.bot.reply_to(message, "Howdy, how are you doing?")

    def send_hi(self, message):
        self.bot.reply_to(message, "hiiiiii")

    def handle_help(self, message):
        help_text = "以下是可用的命令:\n"
        help_text += f"{TelebotCommands.START_COMMAND}: {TelebotCommands.get_command_description(TelebotCommands.START_COMMAND)}\n"
        help_text += f"{TelebotCommands.STOP_COMMAND}: {TelebotCommands.get_command_description(TelebotCommands.STOP_COMMAND)}\n"
        self.bot.reply_to(message, help_text)

    def show_active_strategies(self, message):
        active_strategies = self.strategy_manager.get_active_strategies()
        text = "活跃策略：\n"
        for strategy_name in active_strategies:
            text += f"/{strategy_name}\n"
        self.bot.reply_to(message, text)

    def show_loaded_strategies(self, message):
        loaded_strategies = self.strategy_manager.get_loaded_strategies()
        text = "已加载策略：\n"
        for strategy_name in loaded_strategies:
            text += f"/{strategy_name}\n"
        self.bot.reply_to(message, text)



    def show_strategy_menu(self, message):
        strategy_name = message.text[1:]  # 从命令中提取策略名
        text = f"选择 {strategy_name} 的操作：\n"
        text += "/start - 启动策略\n"
        text += "/stop - 停止策略\n"
        text += "/positions - 展示策略持仓\n"
        text += "/returns - 展示策略收益\n"
        self.bot.reply_to(message, text)







    def run(self):
        self.bot.polling()

    # def handle_start(self, update, context):
    #     chat_id = update.message.chat_id
    #     if chat_id == self.chat_id:
    #         strategy_name = context.args[0] if context.args else None
    #         if strategy_name:
    #             self.strategy_manager.start_strategy(strategy_name)
    #             update.message.reply_text(f"Strategy {strategy_name} started.")
    #         else:
    #             update.message.reply_text("Please provide a strategy name.")
    #     else:
    #         pass
    #
    # def handle_stop(self, update, context):
    #     strategy_name = context.args[0] if context.args else None
    #     if strategy_name:
    #         self.strategy_manager.stop_strategy(strategy_name)
    #         update.message.reply_text(f"Strategy {strategy_name} stopped.")
    #     else:
    #         update.message.reply_text("Please provide a strategy name.")