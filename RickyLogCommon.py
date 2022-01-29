#coding=utf-8

#RickyLuiXY：创建一个通用的日志输出，默认情况下，同时输出到控制台和文件夹中，如果没有的话就创建

import os
import sys
import time
import logging
import logging.handlers

#日志文件名：rlog.txt
#日志级别：INFO及以上

G_logger = logging.getLogger()

def init_log():

    #设置日志级别
    logging.basicConfig(level=logging.NOTSET, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    #创建控制台输出
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    handler_console.setFormatter(log_formatter)
    G_logger.addHandler(handler_console)
    #创建日志文件输出
    cur_path  =  os.getcwd()
    #看当前目录下是否有rlog存在，不存在的话创建一个
    log_path = cur_path+'\\rlog'
    if(os.path.exists(log_path)):
        logging.info('日志目录已存在')
    else:
        os.mkdir(log_path)
    #每次程序运行，创建一个日志
    rq = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    log_filename = log_path+'\\rlog_'+rq+'.log'
    fh = logging.FileHandler(log_filename, mode='w')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(log_formatter)
    G_logger.addHandler(fh)

    pass





if __name__ == "__main__":
    init_log()
    G_logger.info('这是一个日志应用的示例程序')