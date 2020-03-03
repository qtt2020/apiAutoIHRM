import os
import time
import logging, logging.handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = ""
EMP_ID = ""
DEPARTMENT_ID = ""


# 定义初始化日志函数
def init_log():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器 输出到控制台
    sh = logging.StreamHandler()
    # 创建处理器 输出到文件
    log_name = BASE_DIR + "/log/iHRM_{}.log".format(time.strftime("%Y%m%d%H%M%S"))
    th = logging.handlers.TimedRotatingFileHandler(log_name, when="d", interval=1, backupCount=3)
    # 创建格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 将格式器添加到处理器
    th.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(th)
    logger.addHandler(sh)


if __name__ == '__main__':
    init_log()
    logging.info("info级别的日志")
