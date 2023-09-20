# -*- encoding: utf-8 -*-
'''
@File    :   subject.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 12:27    eborlee      1.0         None
'''
from abc import ABC

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)
