# -*- encoding: utf-8 -*-
'''
@File    :   order.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 18:02    eborlee      1.0         None
'''

class Order:
    def __init__(self, symbol, quantity, price, order_type):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.order_type = order_type

    def __str__(self):
        return f"{self.order_type} {self.quantity} {self.symbol} @ {self.price}"
