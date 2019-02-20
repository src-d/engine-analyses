from matplotlib import pyplot as plt
import numpy as np
import pymysql
import time
import coloredlogs, logging

def run(query, host='localhost', user='root', passwd='', log=True):
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db='mysql')
    start = time.time()

    cursor = conn.cursor()
    cursor.execute(query)

    end = time.time()
    if log:
        logging.info("done in %.2f seconds" % (end - start))
    return cursor

def run_one(query, log=True):
    return run(query, log).fetchone()

def run_and_print(query):
    for row in run(query):
        print(*row)