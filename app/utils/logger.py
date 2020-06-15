import logging
import socket
from fluent import asynchandler
from fluent import handler

def process(count, total, speed=2, is_end=False, end_str=''):
    '''显示进度条'''
    percent = int(count * 100 / total)
    percent_cnt = percent // speed
    percent_process = '█' * percent_cnt + ' ' * ((100 // speed) - percent_cnt)
    process_str = '%3d%% |%s|' % (percent, percent_process) + ' ' + end_str
    end = '\r'
    if is_end:
        end = '\r\n'

    print(process_str, end=end)
    return process_str


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def create_fluent_handler(conf):

    ip = get_host_ip()
    level = logging.getLevelName(conf.get('level'))
    __handler = asynchandler.FluentHandler(conf.get('fluent').get('log_name'),
                                      conf.get('fluent').get('host'),
                                      conf.get('fluent').get('port'))
    __handler.setFormatter(handler.FluentRecordFormatter(fmt={
        'ip': ip,
        'from': 'teacher',
        'level': '%(levelname)s',
        'host': '%(hostname)s',
        'server_name': '%(name)s',
        'module': '%(module)s',
        'function': '[%(pathname)s:%(funcName)s:%(lineno)d]',
        'stack_trace': '%(exc_text)s'
    }))
    print('进行到这里')
    __handler.setLevel(level)
    return __handler

def init_logger(conf, function_fmt='[%(pathname)s:%(funcName)s:%(lineno)d]'):
    logger = logging.getLogger(conf.get('server_name'))
    logger.setLevel(conf.get('level'))
    logger.addHandler(create_fluent_handler(conf))

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
        "fluent": {
            "host": host,  # 目前线上集中日志的host
            "port": port,
            "log_name": log_name  # 你的模块日志名@log_name
        }
    }
    return init_logger(logger_config)


'''
def setup_logging(default_path='logging.yaml', default_level=logging.INFO):
    """
        设置日志配置
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)

        info_msg = u"%s自定义加载成功" % default_path
    else:
        logging.basicConfig(level=default_level)
        info_msg = u"%s路径不存在，加载日志配置失败" % default_path
    logger = logging.getLogger()
    logger.info(info_msg)
'''