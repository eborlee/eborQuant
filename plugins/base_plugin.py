# -*- encoding: utf-8 -*-
'''
@File    :   base_plugin.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 19:31    eborlee      1.0         None
'''

# plugin_base.py
from observers.subject import Subject


class PluginBase(Subject):
    def __init__(self):
        super().__init__()

    def run(self):
        raise NotImplementedError
