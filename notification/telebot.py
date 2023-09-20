# -*- encoding: utf-8 -*-
'''
@File    :   telebot.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/20 14:32    eborlee      1.0         None
'''

from observers.observer import Observer
import telebot




class TelegramNotifier(Observer):
    def __init__(self, bot_token, chat_id):
        self.bot = telebot.TeleBot(bot_token)
        self.chat_id = chat_id

    def update(self, msg, **kwargs):
        message = self.build_message(**kwargs)
        if message:
            self.bot.send_message(self.chat_id, message)
            return
        self.bot.send_message(self.chat_id, msg)

    def build_message(self, **kwargs):
        # 根据传入的信息构造要发送的消息
        event_type = kwargs.get('event_type')
        if event_type == 'new_order':
            order_info = kwargs.get('order_info')
            return f"New Order: {order_info}"
        elif event_type == 'portfolio_update':
            portfolio_info = kwargs.get('portfolio_info')
            return f"Portfolio Update: {portfolio_info}"
        return None




