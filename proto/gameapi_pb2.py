# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameapi.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gamebase_pb2 as gamebase__pb2
import gamedebug_pb2 as gamedebug__pb2
import empty_pb2 as empty__pb2
import roomsrv_pb2 as roomsrv__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gameapi.proto',
  package='game.api',
  syntax='proto3',
  serialized_options=b'Z#windplatform/server/protogo/gameapi',
  serialized_pb=b'\n\rgameapi.proto\x12\x08game.api\x1a\x0egamebase.proto\x1a\x0fgamedebug.proto\x1a\x0b\x65mpty.proto\x1a\rroomsrv.proto2J\n\tGameEvent\x12=\n\tGameEvent\x12\x14.game.base.GameEvent\x1a\x14.game.base.GameEvent\"\x00(\x01\x30\x01\x32\x9e\x04\n\x04Game\x12\x41\n\x0cPrepareEnter\x12\x17.game.base.PrepareEnter\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x0cRemovePlayer\x12\x1a.game.base.RemovePlayerReq\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\rUpdateGameCfg\x12\x17.room.srv.RegGameSvrRsp\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\x0b\x41\x64\x64Strategy\x12\x19.game.base.AddStrategyReq\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\x0b\x44\x65lStrategy\x12\x19.game.base.DelStrategyReq\x1a\x16.google.protobuf.Empty\"\x00\x12\x43\n\x0bGetRoomList\x12\x16.google.protobuf.Empty\x1a\x1a.game.debug.GetRoomListRsp\"\x00\x12;\n\tGetPlayer\x12\x18.game.debug.GetPlayerReq\x1a\x12.game.debug.Player\"\x00\x12?\n\nGetSummary\x12\x16.google.protobuf.Empty\x1a\x19.game.debug.GetSummaryRspB%Z#windplatform/server/protogo/gameapib\x06proto3'
  ,
  dependencies=[gamebase__pb2.DESCRIPTOR,gamedebug__pb2.DESCRIPTOR,empty__pb2.DESCRIPTOR,roomsrv__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_GAMEEVENT = _descriptor.ServiceDescriptor(
  name='GameEvent',
  full_name='game.api.GameEvent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=88,
  serialized_end=162,
  methods=[
  _descriptor.MethodDescriptor(
    name='GameEvent',
    full_name='game.api.GameEvent.GameEvent',
    index=0,
    containing_service=None,
    input_type=gamebase__pb2._GAMEEVENT,
    output_type=gamebase__pb2._GAMEEVENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMEEVENT)

DESCRIPTOR.services_by_name['GameEvent'] = _GAMEEVENT


_GAME = _descriptor.ServiceDescriptor(
  name='Game',
  full_name='game.api.Game',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=165,
  serialized_end=707,
  methods=[
  _descriptor.MethodDescriptor(
    name='PrepareEnter',
    full_name='game.api.Game.PrepareEnter',
    index=0,
    containing_service=None,
    input_type=gamebase__pb2._PREPAREENTER,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemovePlayer',
    full_name='game.api.Game.RemovePlayer',
    index=1,
    containing_service=None,
    input_type=gamebase__pb2._REMOVEPLAYERREQ,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGameCfg',
    full_name='game.api.Game.UpdateGameCfg',
    index=2,
    containing_service=None,
    input_type=roomsrv__pb2._REGGAMESVRRSP,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddStrategy',
    full_name='game.api.Game.AddStrategy',
    index=3,
    containing_service=None,
    input_type=gamebase__pb2._ADDSTRATEGYREQ,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DelStrategy',
    full_name='game.api.Game.DelStrategy',
    index=4,
    containing_service=None,
    input_type=gamebase__pb2._DELSTRATEGYREQ,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRoomList',
    full_name='game.api.Game.GetRoomList',
    index=5,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=gamedebug__pb2._GETROOMLISTRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlayer',
    full_name='game.api.Game.GetPlayer',
    index=6,
    containing_service=None,
    input_type=gamedebug__pb2._GETPLAYERREQ,
    output_type=gamedebug__pb2._PLAYER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSummary',
    full_name='game.api.Game.GetSummary',
    index=7,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=gamedebug__pb2._GETSUMMARYRSP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAME)

DESCRIPTOR.services_by_name['Game'] = _GAME

# @@protoc_insertion_point(module_scope)
