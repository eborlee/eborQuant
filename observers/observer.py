# -*- encoding: utf-8 -*-
'''
@File    :   observer.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 12:24    eborlee      1.0         None
'''

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
