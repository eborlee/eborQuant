import asyncio

from core.trade_engine import TradeEngine



credentials = {
    'apiKey': 'LfguEFUhFT9EBfjs8mmdRVRFrLgpm4utZb1zPcVw9pzBjA6UTVdGPdANJzkBhGQG',
    'secret': 'ATvcAWKUPPLHN7uFulk3l1gj6w4gsNTJJ5Hw3r6HUSnW6iebDaSG0fJkmmzgoxsj'
}

symbols = ['BTC/USDT','ETH/USDT']
engine = TradeEngine("binance", credentials)
loop = asyncio.get_event_loop()
result = loop.run_until_complete(engine.get_klines(symbols, '15m'))
print(result)