import logging
import socket
from fluent import asynchandler
from fluent import handler


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def init_logger(conf, function_fmt='[%(pathname)s:%(funcName)s:%(lineno)d]'):
    logger = logging.getLogger(conf.get('server_name'))
    logger.setLevel(conf.get('level'))

    #此处用于打印
    __stream_handler = logging.StreamHandler()
    __stream_handler.setFormatter(logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s] ' + function_fmt + '%(message)s'))
    __stream_handler.setLevel(conf.get('level'))
    logger.addHandler(__stream_handler)

    return logger

def create_logger(log_name, category, level="DEBUG", host="127.0.0.1", port=24224,
                  function_fmt='[%(pathname)s:%(funcName)s:%(lineno)d]'):
    logger_config = {
        "server_name": category,  # 你的日志分类
        "level": "DEBUG",
    }
    return init_logger(logger_config)


