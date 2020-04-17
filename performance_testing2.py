#!/usr/env/bin python3
# -*- coding:utf-8 -*-
import protocol_client
import pymysql
import time
import threading


def con_mysql(user_number):
    db = pymysql.connect('10.0.0.32', 'root', '123456', 'game', 3306)
    cursor = db.cursor()
    sql = 'select user_name from user_info where id between 1545 and {}'.format(user_number + 1544)
    cursor.execute(sql)
    userToken = cursor.fetchall()
    db.commit()
    db.close()
    return userToken


def Concurrent(num):
    client = protocol_client.protocol_client()
    Threads = []
    userTokenlist = list(con_mysql(num))
    for i in userTokenlist:
        th = threading.Thread(target=client.loginhall, args=(i,))
        th.setDaemon(True)
        Threads.append(th)
    for th in Threads:
        th.start()
    print("当前耗时为：%ss" % time.process_time())
    while True:
        time.sleep(5)
        client.countuser()
    # for th in Threads:
    #     th.join()


if __name__ == "__main__":
    playerlist = [50,50,50,50]
    Concurrent(130)



