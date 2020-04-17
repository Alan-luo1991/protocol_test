#!/usr/env/bin python3
# -*- coding:utf-8 -*-

from websocket import *
from google.protobuf.json_format import MessageToJson
import proto.any_pb2
import proto.gwapiwb_pb2
import json, time, base64
import threading
import pymysql
from greenlet import greenlet


def a():
    print(111)

timer1 = threading.Timer(3, a)
timer1.start()