# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamesss.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gamebase_pb2 as gamebase__pb2
import gamecard_pb2 as gamecard__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamesss.proto',
  package='game.sss',
  syntax='proto3',
  serialized_options=b'Z#windplatform/server/protogo/gamesss',
  serialized_pb=b'\n\rgamesss.proto\x12\x08game.sss\x1a\x0egamebase.proto\x1a\x0egamecard.proto\"L\n\tCardArray\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.game.sss.CardType\x12\x1d\n\x04\x63\x61rd\x18\x02 \x03(\x0b\x32\x0f.game.card.Card\"K\n\nPlayerItem\x12+\n\x0bplayerAttri\x18\x01 \x01(\x0b\x32\x16.game.base.PlayerAttri\x12\x10\n\x08\x61vatarID\x18\x02 \x01(\x05\"3\n\nWaterLevel\x12\x10\n\x08waterNum\x18\x01 \x03(\x05\x12\x13\n\x0bwaterAddNum\x18\x02 \x03(\x05\"U\n\x08GameInfo\x12$\n\x06player\x18\x01 \x03(\x0b\x32\x14.game.sss.PlayerItem\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.game.sss.GameStaus\"4\n\x0b\x44isplayInfo\x12%\n\x08\x63\x61rdInfo\x18\x01 \x03(\x0b\x32\x13.game.sss.CardArray\"n\n\rCompareResult\x12%\n\x08\x63\x61rdInfo\x18\x01 \x03(\x0b\x32\x13.game.sss.CardArray\x12\'\n\twaterInfo\x18\x02 \x03(\x0b\x32\x14.game.sss.WaterLevel\x12\r\n\x05money\x18\x03 \x01(\x03\"\r\n\x0bGamingStaus\"\x1e\n\rOpenGamingReq\x12\r\n\x05index\x18\x01 \x01(\x05\"\x8d\x01\n\x10OpenGamingResult\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x31\n\x06\x62\x65tEnd\x18\x02 \x01(\x0e\x32!.game.sss.OpenGamingResult.BetEnd\"7\n\x06\x42\x65tEnd\x12\x0b\n\x07XIE_XIE\x10\x00\x12\t\n\x05\x46IRST\x10\x01\x12\n\n\x06SECOND\x10\x02\x12\t\n\x05THIRD\x10\x03*E\n\tGameStaus\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0b\n\x07\x44ISPLAY\x10\x02\x12\x07\n\x03\x45ND\x10\x03\x12\n\n\x06GAMING\x10\x04*\xcc\x02\n\x08\x43\x61rdType\x12\x10\n\x0ctype_default\x10\x00\x12\x0b\n\x07type_wl\x10\x01\x12\x0b\n\x07type_dz\x10\x02\x12\x0b\n\x07type_ld\x10\x03\x12\x0b\n\x07type_st\x10\x04\x12\x0b\n\x07type_sz\x10\x05\x12\x0b\n\x07type_th\x10\x06\x12\x0b\n\x07type_hl\x10\x07\x12\x0b\n\x07type_tz\x10\x08\x12\x0c\n\x08type_ths\x10\t\x12\x0c\n\x08type_sth\x10\n\x12\x0c\n\x08type_ssz\x10\x0b\x12\x0c\n\x08type_ldb\x10\x0c\x12\r\n\ttype_wdst\x10\r\x12\r\n\ttype_stst\x10\x0e\x12\x0c\n\x08type_cys\x10\x0f\x12\x0b\n\x07type_qx\x10\x10\x12\x0b\n\x07type_qd\x10\x11\x12\r\n\ttype_sftx\x10\x12\x12\r\n\ttype_sths\x10\x13\x12\r\n\ttype_srhz\x10\x14\x12\x0c\n\x08type_ltl\x10\x15\x12\r\n\ttype_zzql\x10\x16*\x9e\x01\n\x05\x45vent\x12\x10\n\x0cPLACE_HOLDER\x10\x00\x12\x12\n\x0b\x44ISPLAY_REQ\x10\x81\x80\xd0\x03\x12\x15\n\x0e\x43OMPARE_RESULT\x10\x82\x80\xd0\x03\x12\x13\n\x0cGAMING_STAUS\x10\x83\x80\xd0\x03\x12\x16\n\x0fOPEN_GAMING_REQ\x10\x84\x80\xd0\x03\x12\x19\n\x12OPEN_GAMING_RESULT\x10\x85\x80\xd0\x03\x12\x10\n\tSEND_CARD\x10\x86\x80\xd0\x03\x42%Z#windplatform/server/protogo/gamesssb\x06proto3'
  ,
  dependencies=[gamebase__pb2.DESCRIPTOR,gamecard__pb2.DESCRIPTOR,])

_GAMESTAUS = _descriptor.EnumDescriptor(
  name='GameStaus',
  full_name='game.sss.GameStaus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAMING', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=711,
  serialized_end=780,
)
_sym_db.RegisterEnumDescriptor(_GAMESTAUS)

GameStaus = enum_type_wrapper.EnumTypeWrapper(_GAMESTAUS)
_CARDTYPE = _descriptor.EnumDescriptor(
  name='CardType',
  full_name='game.sss.CardType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='type_default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_wl', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_dz', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_ld', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_st', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_sz', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_th', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_hl', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_tz', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_ths', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_sth', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_ssz', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_ldb', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_wdst', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_stst', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_cys', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_qx', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_qd', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_sftx', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_sths', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_srhz', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_ltl', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='type_zzql', index=22, number=22,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=783,
  serialized_end=1115,
)
_sym_db.RegisterEnumDescriptor(_CARDTYPE)

CardType = enum_type_wrapper.EnumTypeWrapper(_CARDTYPE)
_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='game.sss.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLACE_HOLDER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_REQ', index=1, number=7602177,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPARE_RESULT', index=2, number=7602178,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAMING_STAUS', index=3, number=7602179,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_GAMING_REQ', index=4, number=7602180,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_GAMING_RESULT', index=5, number=7602181,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_CARD', index=6, number=7602182,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1118,
  serialized_end=1276,
)
_sym_db.RegisterEnumDescriptor(_EVENT)

Event = enum_type_wrapper.EnumTypeWrapper(_EVENT)
Default = 0
READY = 1
DISPLAY = 2
END = 3
GAMING = 4
type_default = 0
type_wl = 1
type_dz = 2
type_ld = 3
type_st = 4
type_sz = 5
type_th = 6
type_hl = 7
type_tz = 8
type_ths = 9
type_sth = 10
type_ssz = 11
type_ldb = 12
type_wdst = 13
type_stst = 14
type_cys = 15
type_qx = 16
type_qd = 17
type_sftx = 18
type_sths = 19
type_srhz = 20
type_ltl = 21
type_zzql = 22
PLACE_HOLDER = 0
DISPLAY_REQ = 7602177
COMPARE_RESULT = 7602178
GAMING_STAUS = 7602179
OPEN_GAMING_REQ = 7602180
OPEN_GAMING_RESULT = 7602181
SEND_CARD = 7602182


_OPENGAMINGRESULT_BETEND = _descriptor.EnumDescriptor(
  name='BetEnd',
  full_name='game.sss.OpenGamingResult.BetEnd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='XIE_XIE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECOND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIRD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=654,
  serialized_end=709,
)
_sym_db.RegisterEnumDescriptor(_OPENGAMINGRESULT_BETEND)


_CARDARRAY = _descriptor.Descriptor(
  name='CardArray',
  full_name='game.sss.CardArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='game.sss.CardArray.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card', full_name='game.sss.CardArray.card', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=135,
)


_PLAYERITEM = _descriptor.Descriptor(
  name='PlayerItem',
  full_name='game.sss.PlayerItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerAttri', full_name='game.sss.PlayerItem.playerAttri', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatarID', full_name='game.sss.PlayerItem.avatarID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=212,
)


_WATERLEVEL = _descriptor.Descriptor(
  name='WaterLevel',
  full_name='game.sss.WaterLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waterNum', full_name='game.sss.WaterLevel.waterNum', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterAddNum', full_name='game.sss.WaterLevel.waterAddNum', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=265,
)


_GAMEINFO = _descriptor.Descriptor(
  name='GameInfo',
  full_name='game.sss.GameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='game.sss.GameInfo.player', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='game.sss.GameInfo.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=352,
)


_DISPLAYINFO = _descriptor.Descriptor(
  name='DisplayInfo',
  full_name='game.sss.DisplayInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardInfo', full_name='game.sss.DisplayInfo.cardInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=406,
)


_COMPARERESULT = _descriptor.Descriptor(
  name='CompareResult',
  full_name='game.sss.CompareResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardInfo', full_name='game.sss.CompareResult.cardInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterInfo', full_name='game.sss.CompareResult.waterInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='game.sss.CompareResult.money', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=518,
)


_GAMINGSTAUS = _descriptor.Descriptor(
  name='GamingStaus',
  full_name='game.sss.GamingStaus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=533,
)


_OPENGAMINGREQ = _descriptor.Descriptor(
  name='OpenGamingReq',
  full_name='game.sss.OpenGamingReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='game.sss.OpenGamingReq.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=565,
)


_OPENGAMINGRESULT = _descriptor.Descriptor(
  name='OpenGamingResult',
  full_name='game.sss.OpenGamingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='game.sss.OpenGamingResult.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='betEnd', full_name='game.sss.OpenGamingResult.betEnd', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENGAMINGRESULT_BETEND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=709,
)

_CARDARRAY.fields_by_name['type'].enum_type = _CARDTYPE
_CARDARRAY.fields_by_name['card'].message_type = gamecard__pb2._CARD
_PLAYERITEM.fields_by_name['playerAttri'].message_type = gamebase__pb2._PLAYERATTRI
_GAMEINFO.fields_by_name['player'].message_type = _PLAYERITEM
_GAMEINFO.fields_by_name['status'].enum_type = _GAMESTAUS
_DISPLAYINFO.fields_by_name['cardInfo'].message_type = _CARDARRAY
_COMPARERESULT.fields_by_name['cardInfo'].message_type = _CARDARRAY
_COMPARERESULT.fields_by_name['waterInfo'].message_type = _WATERLEVEL
_OPENGAMINGRESULT.fields_by_name['betEnd'].enum_type = _OPENGAMINGRESULT_BETEND
_OPENGAMINGRESULT_BETEND.containing_type = _OPENGAMINGRESULT
DESCRIPTOR.message_types_by_name['CardArray'] = _CARDARRAY
DESCRIPTOR.message_types_by_name['PlayerItem'] = _PLAYERITEM
DESCRIPTOR.message_types_by_name['WaterLevel'] = _WATERLEVEL
DESCRIPTOR.message_types_by_name['GameInfo'] = _GAMEINFO
DESCRIPTOR.message_types_by_name['DisplayInfo'] = _DISPLAYINFO
DESCRIPTOR.message_types_by_name['CompareResult'] = _COMPARERESULT
DESCRIPTOR.message_types_by_name['GamingStaus'] = _GAMINGSTAUS
DESCRIPTOR.message_types_by_name['OpenGamingReq'] = _OPENGAMINGREQ
DESCRIPTOR.message_types_by_name['OpenGamingResult'] = _OPENGAMINGRESULT
DESCRIPTOR.enum_types_by_name['GameStaus'] = _GAMESTAUS
DESCRIPTOR.enum_types_by_name['CardType'] = _CARDTYPE
DESCRIPTOR.enum_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CardArray = _reflection.GeneratedProtocolMessageType('CardArray', (_message.Message,), {
  'DESCRIPTOR' : _CARDARRAY,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.CardArray)
  })
_sym_db.RegisterMessage(CardArray)

PlayerItem = _reflection.GeneratedProtocolMessageType('PlayerItem', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERITEM,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.PlayerItem)
  })
_sym_db.RegisterMessage(PlayerItem)

WaterLevel = _reflection.GeneratedProtocolMessageType('WaterLevel', (_message.Message,), {
  'DESCRIPTOR' : _WATERLEVEL,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.WaterLevel)
  })
_sym_db.RegisterMessage(WaterLevel)

GameInfo = _reflection.GeneratedProtocolMessageType('GameInfo', (_message.Message,), {
  'DESCRIPTOR' : _GAMEINFO,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.GameInfo)
  })
_sym_db.RegisterMessage(GameInfo)

DisplayInfo = _reflection.GeneratedProtocolMessageType('DisplayInfo', (_message.Message,), {
  'DESCRIPTOR' : _DISPLAYINFO,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.DisplayInfo)
  })
_sym_db.RegisterMessage(DisplayInfo)

CompareResult = _reflection.GeneratedProtocolMessageType('CompareResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPARERESULT,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.CompareResult)
  })
_sym_db.RegisterMessage(CompareResult)

GamingStaus = _reflection.GeneratedProtocolMessageType('GamingStaus', (_message.Message,), {
  'DESCRIPTOR' : _GAMINGSTAUS,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.GamingStaus)
  })
_sym_db.RegisterMessage(GamingStaus)

OpenGamingReq = _reflection.GeneratedProtocolMessageType('OpenGamingReq', (_message.Message,), {
  'DESCRIPTOR' : _OPENGAMINGREQ,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.OpenGamingReq)
  })
_sym_db.RegisterMessage(OpenGamingReq)

OpenGamingResult = _reflection.GeneratedProtocolMessageType('OpenGamingResult', (_message.Message,), {
  'DESCRIPTOR' : _OPENGAMINGRESULT,
  '__module__' : 'gamesss_pb2'
  # @@protoc_insertion_point(class_scope:game.sss.OpenGamingResult)
  })
_sym_db.RegisterMessage(OpenGamingResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
