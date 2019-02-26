from contextlib import contextmanager
import logging
import time

import coloredlogs
from matplotlib import pyplot
import numpy
import pymysql

logger = logging.getLogger("run")

@contextmanager
def no_logs():
    level = logger.level
    logger.setLevel(logging.WARN)
    try:
        yield None
    finally:
        logger.setLevel(level)

def run(query, host="localhost", user="root", passwd=""):
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db="mysql")
    
    start = time.time()
    cursor = conn.cursor()
    cursor.execute(query)
    end = time.time()
    
    logger.info("done in %.2f seconds" % (end - start))
    return cursor

def run_one(query, log=True):
    return run(query, log).fetchone()

def run_and_print(query):
    for row in run(query):
        print(*row)