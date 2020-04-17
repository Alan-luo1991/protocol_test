#!/usr/env/bin python3
# -*- coding:utf-8 -*-
from websocket import *
from google.protobuf.json_format import MessageToJson
import proto.any_pb2
import proto.gwapiwb_pb2
import json, time, base64
try:
    import thread
except ImportError:
    import _thread as thread


class gateway_client:
    def __init__(self, url):
        self.url = url

    def connect(self):
        url = self.url
        try:
            ws = create_connection(url=url)
            logging.info("Connect to websocketserver successfully!")
            return ws
        except:
            logging.info("Failed to connect to websocketserver!")
            return ""

    def send(self, wsObj, message):
        if not wsObj or not message:
            logging.error("Parameter Error!")
            return "NO"
        try:
            wsObj.send(message)
        except:
            logging.error("Failed to send message to websocketserver!")
            return

    def recv(self, wsObj):
        while 1:
            res = wsObj.recv()
            print(res)

    def main(self):
        ws = self.connect()
        if ws != "":
            self.recv(ws)


if __name__ == '__main__':
    client = gateway_client("ws://10.0.0.204:31810/63OYS8FURX6YQ2K8AGC54QZP16UOBP25WD6NVW5VCTZ4HR2ODT7DDDMXR7IAY9K7/game/10.0.0.206:30311:32368")
    client.main()
