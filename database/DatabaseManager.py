# -*- encoding: utf-8 -*-
'''
@File    :   DatabaseManager.py  
  
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/19 11:52    eborlee      1.0         None
'''
import psycopg2
from psycopg2 import pool
from observers.observer import Observer
from observers.subject import Subject


class DatabaseManager(Observer, Subject):
    def __init__(self, config, minconn=1, maxconn=10):
        super().__init__()
        database_url = f"dbname='{config['dbname']}' " \
                       f"user='{config['username']}' " \
                       f"host='{config['host']}' " \
                       f"password='{config['password']}' " \
                       f"port='{config['port']}'"

        self.connection_pool = psycopg2.pool.SimpleConnectionPool(minconn, maxconn, database_url)

    def update(self, message):
        # 根据消息类型调用相应的处理方法
        handler_method = getattr(self, f"handle_{message['type']}", None)
        if handler_method:
            handler_method(message['data'])

    def handle_trade(self, data):
        self._execute_sql("INSERT INTO trades (...) VALUES (...)", data)

    def handle_strategy_net_value(self, data):
        self._execute_sql("INSERT INTO strategy_net_values (...) VALUES (...)", data)

    def handle_strategy_summary(self, data):
        self._execute_sql("INSERT INTO strategy_summaries (...) VALUES (...)", data)

    def _execute_sql(self, query, params):
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cursor:
                conn.autocommit = False  # 关闭自动提交
                try:
                    cursor.execute(query, params)
                    conn.commit()  # 提交事务
                except Exception as e:
                    conn.rollback()  # 回滚事务

                    raise e  # 重新抛出异常
        finally:
            self.connection_pool.putconn(conn)

    def add_strategy(self, strategy_data):
        columns = ', '.join(strategy_data.keys())
        placeholders = ', '.join(['%s'] * len(strategy_data))

        query = f"""INSERT INTO strategies ({columns})
                        VALUES ({placeholders})
                        ON CONFLICT (strategy_id) DO NOTHING;"""  # 如果strategy_name存在，则不插入

        params = tuple(strategy_data.values())

        try:
            self._execute_sql(query, params)
        except Exception as e:
            self.notify_observers(f"数据库操作触发异常:{e}")

    def update_strategy(self, strategy_id, last_started_time, status):
        query = """UPDATE strategies
                   SET last_started_time = %s, status = %s
                   WHERE strategy_id = %s;"""
        params = (last_started_time, status, strategy_id)

        try:
            self._execute_sql(query, params)
        except Exception as e:
            self.notify_observers(f"数据库操作触发异常:{e}")

    def close(self):
        self.connection_pool.closeall()