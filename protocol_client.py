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


class protocol_client:

    def __init__(self):
        self._online = 0
        self._killnub = 0

    # 将pdstring转化为json
    def pb_to_json(self):
        req = proto.gwapiwb_pb2.GameEvent()
        req.ParseFromString(self)
        jsonStringNTF= MessageToJson(req)
        return jsonStringNTF

    def Any(self):
        Any = proto.any_pb2.Any()
        Any.type_url = 'type.googleapis.com/' + 'GameEvent'
        return Any

    def GameEvent(self, mstype, playerToken):
        GameEvent = proto.gwapiwb_pb2.GameEvent()
        GameEvent.type = mstype
        GameEvent.playerToken = playerToken
        return GameEvent.SerializeToString()

    def loginhall(self, userToken):
        socket_lock = threading.Lock()
        url_ddz = 'ws://10.0.0.203:32642/{}/game/10.0.0.204:30016:30250'.format(userToken)
        ws = create_connection(url_ddz, timeout=10)
        playerToken = ""
        try:
            socket_lock.acquire()
            result = ws.recv_data()
            result = protocol_client.pb_to_json(result[1])
            result = json.loads(result)
            print(result)
            playerToken = result['playerToken']
            socket_lock.release()
            ws.send(protocol_client.GameEvent(self, -14, playerToken), opcode=ABNF.OPCODE_BINARY)
            ws.send(protocol_client.GameEvent(self, -16, playerToken), opcode=ABNF.OPCODE_BINARY)
            ws.send(protocol_client.GameEvent(self, -15, playerToken), opcode=ABNF.OPCODE_BINARY)
            self._online += 1
        except:
            print("无法连接到游戏")
            self._killnub += 1
        try:
            while True:
                time.sleep(3)
                ws.send(protocol_client.GameEvent(self, -21, playerToken), opcode=ABNF.OPCODE_BINARY)
                socket_lock.acquire()
                result = ws.recv_data()
                result = protocol_client.pb_to_json(result[1])
                result = json.loads(result)
                socket_lock.release()
                if result['type'] == -21:
                    print(playerToken + '：心跳连接中')
                else:
                    print(result)
        except:
            print(playerToken + ": 心跳断开!!!")
            self._killnub += 1
            self._online -= 1

    def countuser(self):
        print("当前在线用户数量：{}".format(self._online))
        print("当前断开用户数量：{}".format(self._killnub))


if __name__ == "__main__":
    userToken1 = '1E15BNMPXTUK4T9SM9YLZEF9D56SHRBVKW57A2RM8F21HZ7MQ6JPY3BE32TBLNOD'
    userToken2 = 'AQPPXPIA7FJ4FL7ZX3189I5ZIBKKLCAXS5CQG9HUW7T8YSS8GAVXEKQSL3TPHVT6'
    a = protocol_client()
    t1 = threading.Thread(target=a.loginhall, args=(userToken1,))
    t2 = threading.Thread(target=a.loginhall, args=(userToken2,))
    t1.start()
    t2.start()
    t1.join(1)
    while True:
        time.sleep(3)
        a.countuser()
    # while True:
    #     time.sleep(5)
    #     a.countuser()