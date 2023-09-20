# -*- encoding: utf-8 -*-
'''
@File    :   config.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/20 15:27    eborlee      1.0         None
'''
import yaml



class ConfigLoader:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)

    def load_config(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as file:
            config = yaml.safe_load(file)
        return config

    def get_config(self, key=None):
        if key:
            return self.config.get(key)
        return self.config

    def get_global_param(self, param):
        return self.config['global'][param]

    def get_notifications_param(self, param):
        return self.config['notifications'][param]

    def get_strategy_param(self, strategy_name, param):
        return self.config['strategies'][strategy_name][param]

    def get_db_params(self):
        return self.config['database']

# config = Config('global_config.yaml')
# log_level = config.get_global_param('log_level')
# CTA_param1 = config.get_strategy_param('CTA_strategy', 'param1')
