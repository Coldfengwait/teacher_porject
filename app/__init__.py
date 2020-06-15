#coding: utf8
from flask import Flask, session, g, url_for, request, redirect, jsonify

import os
from celery import Celery
from flask_cors import CORS
import redis
from flask_sqlalchemy import SQLAlchemy
# from raven.contrib.flask import Sentry
from .utils import create_logger

# if 'CONFIG' not in os.environ:
#     raise Exception(u'需要设置环境变量CONFIG 参数值是config.Online 或者config.Test')

app = Flask(__name__)

config = 'config.Test'#os.environ['CONFIG']
app.config.from_object( config )
#设置admin为中文
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
app.jinja_env.filters['join_pgy_base_url'] = lambda v: v % app.config['PGY_BASE_URL']
CORS(app, supports_credentials=True)

db = SQLAlchemy(app)

# Sentry上报
# sentry = Sentry()
# if config == "config.Config":
#     sentry.init_app(app)

# 异步队列
celery = Celery(__name__, broker=app.config['REDIS_FOR_CELERY'], backend=app.config['REDIS_FOR_CELERY'])

celery.conf.update(app.config)

celery.conf.update({
    "task_soft_time_limit": 60,
    "task_time_limit": 120,
    "worker_max_tasks_per_child": 1000,
    "result_backend": app.config['CELERY_RESULT_BACKEND_CONFIG'],
})


# 全局缓存redis 句柄
app.cache_redis = redis.StrictRedis(**app.config['DATA_CACHE_REDIS'])


logger = create_logger(app.config['LOG_NAME'], app.config['LOG_CATEGORY'])



from app import models
from app import views

# 上报到监控系统
# if config == "config.Config":
#     Statsd().init_app(app)

#####here:添加模块##########
# from app import test

# from app import wxauth
# from app import weike_pay

@app.before_request
def before_request():
    if request.path.startswith('/admin') or request.path.startswith('/static'):
        return

    if 'X-Forwarded-For' in request.headers:
        g.remote_ip = request.headers.getlist("X-Forwarded-For")[0].rpartition(' ')[-1]
    else:
        g.remote_ip = request.remote_addr or '127.0.0.1'


