import os


def get_path(rpath):
    LOCAL_DIR = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(LOCAL_DIR, rpath))


class Online(object):
    pass


class Test(object):
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:123456@127.0.0.1:3306/teacher?charset=utf8mb4"
    # 自动回收连接的秒数。这对 MySQL 是必须的
    SQLALCHEMY_POOL_RECYCLE=3600
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # 设置自动提交然后关闭连接
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    # 最大数据库池的大小。 默认与数据库引擎的值相同 (通常为 5)
    # SQLALCHEMY_POOL_SIZE = 5
    # 控制连接池达到最大大小后还可以创建的连接数，当这些附加连接返回到连接池时，它们将会被断开并丢弃。
    # SQLALCHEMY_MAX_OVERFLOW = 30
    # 查询时会显示原始SQL语句
    # SQLALCHEMY_ECHO =True
    # Celery Redis使用的是0通道的
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/1"
    CELERY_RESULT_BACKEND_CONFIG = "redis://127.0.0.1:6379/1"
    CELERY_TASKS_NAME = ""
    REDIS_FOR_CELERY = "redis://127.0.0.1:6379/1"
    # 缓存数据使用的redis
    DATA_CACHE_REDIS = {
        "host": "127.0.0.1",
        "port": 6379,
        "db": 1,
    }
    LOG_NAME = 'teacher'
    LOG_CATEGORY = 'dev'
    SECRET_KEY = "fdfasdasdasdsadsadsadsa"
    JWT_SECRET_KEY = "#sdas#32423adsadsad&YAN"

