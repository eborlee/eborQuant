# -*- encoding: utf-8 -*-
'''
@File    :   t.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/9/11 1:01    eborlee      1.0         None
'''
import asyncio

from core.trade_engine import TradeEngine


if __name__ == "__main__":
    credentials = {
        'apiKey': 'LfguEFUhFT9EBfjs8mmdRVRFrLgpm4utZb1zPcVw9pzBjA6UTVdGPdANJzkBhGQG',
        'secret': 'ATvcAWKUPPLHN7uFulk3l1gj6w4gsNTJJ5Hw3r6HUSnW6iebDaSG0fJkmmzgoxsj'
    }

    symbols = ['BTC/USDT','ETH/USDT']
    engine = TradeEngine("binance", credentials)
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(engine.get_klines(symbols, '15m', limit=2))
    print(result)
    loop.run_until_complete(engine.exchange.close())
