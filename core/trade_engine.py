# -*- encoding: utf-8 -*-
'''
@File    :   trade_engine.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 12:27    eborlee      1.0         None
'''
import asyncio

from observers.subject import Subject
import ccxt
import ccxt.async_support as ccxt_async


class TradeEngine(Subject):
    def __init__(self, exchange_name, credentials):
        super().__init__()
        # 通过动态获取属性以动态选择交易所方法
        self.exchange = getattr(ccxt_async, exchange_name)({
            'apiKey': credentials['apiKey'],
            'secret': credentials['secret'],

            'enableRateLimit': True,
            'options': {
                'defaultType': 'future',
                # 'adjustForTimeDifference': True,
                # 'test': True, # 开启Testnet环境
            }
        })

    def order(self, order):
        # Translate the custom Order object into the format expected by ccxt
        ccxt_order = {
            'symbol': order.symbol,
            'type': order.order_type.lower(),
            'side': 'buy' if order.quantity > 0 else 'sell',
            'amount': abs(order.quantity),
            'price': order.price
        }

        # Execute the order using ccxt
        result = self.exchange.create_order(**ccxt_order)

        # Notify all observers with the result
        self.notify_observers(result)

    def balance(self):
        # Retrieve the balance from the exchange using ccxt
        return self.exchange.fetch_balance()

    # Additional methods for querying order status, fetching historical data, etc.

    # def get_klines(self, symbol, timeframe='1m', since=None, limit=None):
    #     """
    #     Fetches the K-line data for the given symbol and timeframe.
    #
    #     :param symbol: The trading pair symbol, e.g., 'BTC/USDT'
    #     :param timeframe: Timeframe for the K-line data, e.g., '1m', '5m', '1h', etc.
    #     :param since: Timestamp for filtering the results (optional)
    #     :param limit: Number of K-line data points to fetch (optional)
    #     :return: List of K-line data
    #     """
    #     if self.exchange.has['fetchOHLCV']:
    #         ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    #         return ohlcv
    #     else:
    #         raise Exception(f"{self.exchange.id} does not support fetching OHLCV data")

    async def get_kline(self, symbol, timeframe='1d', limit=1):
        data = await self.exchange.fetch_ohlcv(symbol=symbol,
                                               timeframe=timeframe,
                                               limit=limit)

        return data

    async def get_klines(self, symbols, timeframe='1d', limit=1):
        tasks = [self.get_kline(symbol, timeframe, limit) for symbol in symbols]

        return await asyncio.gather(*tasks)
