import logging
import os
import time
class Logger(object):
    def __init__(self, logger="Root"):  # logger的类名，默认为Root
        # 创建logger并设置日志等级
        # 日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG) # DEBUG以及以上等级写入日志
        """
        # 设置保存本地得日志文件名
        # os.getcwd()获得项目所在的当前目录
        # os.path.dirname(path):去掉文件名返回目录，os,path.dirname(__file__):当前文件的绝对路径
        """
        log_path = os.path.dirname(os.getcwd()) + '\log\ '
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_name = log_path + rq + '.log'
        print(log_name)
        # 设置日志的输出格式
        fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 创建输出到本地文件得handle，FileHandler
        fh = logging.FileHandler(log_name, 'a')  # 日志写入式追加模式
        fh.setLevel(logging.INFO) # 只有WARNING级别得会写入到日志中
        fh.setFormatter(fomatter) # 定义写入到本地文件得日志格式
        self.logger.addHandler(fh)
        # 创建用于输出到控制台得StreamHandler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fomatter)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger