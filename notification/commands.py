# -*- encoding: utf-8 -*-
'''
@File    :   commands.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/22 18:41    eborlee      1.0         None
'''

class TelebotCommands:
    INIT_WORDS = "=====================\n" +\
                 "Trading Framework activated\n" +\
                 "=====================\n" +\
                 "/hi: 检测主框架运行情况\n" +\
                "/help: 查看策略交互命令列表\n" +\
                "/loaded: 查看已加载策略\n" +\
                "/running: 查看正在运行策略\n" +\
                "/exit: 终止主程序\n"
    START_COMMAND = "/start"
    STOP_COMMAND = "/stop"

    @staticmethod
    def get_command_description(command):
        descriptions = {

            TelebotCommands.START_COMMAND: "启动策略",
            TelebotCommands.STOP_COMMAND: "停止策略",
        }
        return descriptions.get(command, "未知命令")
