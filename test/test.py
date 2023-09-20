# -*- encoding: utf-8 -*-
'''
@File    :   test.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/20 20:25    eborlee      1.0         None
'''

# from configs.config import Config
#
# import telebot
# import os
# print(os.getpid())
#
#
#
#
#
# config = Config("../configs/sys_config.yaml")
#
# bot_token = config.config['notifications']['telegram']['bot_token']
# chatid =  config.config['notifications']['telegram']['chat_id']
# bot = telebot.TeleBot(bot_token)
# bot.send_message(chatid, 'aaa')

# import pickle
# from multiprocessing import Process
#
# def foo():
#     print("Hello")
#
# p = Process(target=foo)
# pickled = pickle.dumps(p)

import ccxt
# import socket
# #
# # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # s.connect(('10.254.254.254',1))
# # print(s.getsockname()[0])
#
exchange = getattr(ccxt, "binance")({
            # 'apiKey': credentials['apiKey'],
            # 'secret': credentials['secret'],
            'apiKey': 'LfguEFUhFT9EBfjs8mmdRVRFrLgpm4utZb1zPcVw9pzBjA6UTVdGPdANJzkBhGQG',
            'secret': 'ATvcAWKUPPLHN7uFulk3l1gj6w4gsNTJJ5Hw3r6HUSnW6iebDaSG0fJkmmzgoxsj',

                'options': {
                    'defaultType': 'future',
                    # 'adjustForTimeDifference': True,
                    # 'test': True, # 开启Testnet环境
            }
        })
#
print("余额:", exchange.fetch_balance())
# from loggers.logger import Logger
#
# logger = Logger('../app.log')
#
# logger.update({
#     "type":"INFO",
#     "data":"123445"
# })


# import requests
#
# url = 'https://api.binance.com/api/v1/ticker/price'
#
# # 发送GET请求
# response = requests.get(url)
#
# # 检查响应
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"HTTP请求失败，状态码：{response.status_code}")
