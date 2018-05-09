# -*- coding: UTF-8 -*-


class Log:
    def __init__(self):
        print("init Log")

    @staticmethod
    def d(log_str):
        if type(log_str) is not str:
            log_str = str(log_str)
        print(log_str)
