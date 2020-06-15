# encoding: utf8
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from app import models, app, db
from app import logger
import datetime
import logging


log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)


def AutoHandler():
    """自动任务"""
    logger.debug("[AutoHandler] 开始")

    print("做对应的任务")
    logger.debug("[AutoHandler]结束")


executors = {
    'default': ThreadPoolExecutor(8),
}

sched = BlockingScheduler(executors=executors)

sched.add_job(AutoHandler, 'interval', seconds=3, start_date='2020-6-15 11:00:00')

if __name__ == "__main__":
    sched.start()
