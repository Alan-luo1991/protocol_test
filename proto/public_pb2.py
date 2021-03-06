# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import any_pb2 as any__pb2
import empty_pb2 as empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='public.proto',
  package='public',
  syntax='proto3',
  serialized_options=b'Z\"windplatform/server/protogo/public',
  serialized_pb=b'\n\x0cpublic.proto\x12\x06public\x1a\tany.proto\x1a\x0b\x65mpty.proto\">\n\nClientData\x12\x10\n\x08playerID\x18\x01 \x01(\t\x12\x0e\n\x06gwName\x18\x02 \x01(\t\x12\x0e\n\x06ipAddr\x18\x03 \x01(\t\"a\n\x0ePlayerBaseInfo\x12\x10\n\x08playerID\x18\x01 \x01(\t\x12\x10\n\x08nickName\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\x05\x12\r\n\x05money\x18\x04 \x01(\x03\x12\x0c\n\x04seat\x18\x05 \x01(\x05\"\xc0\x01\n\x07GameCfg\x12\x10\n\x08kickTime\x18\x01 \x01(\x05\x12\x1a\n\x12waitTimeBeforStart\x18\x02 \x01(\x05\x12\x12\n\nminUserCnt\x18\x03 \x01(\x05\x12\x12\n\nmaxUserCnt\x18\x04 \x01(\x05\x12\x15\n\rwaterLevelWin\x18\x05 \x01(\x05\x12\x16\n\x0ewaterLevelLose\x18\x06 \x01(\x05\x12\x0b\n\x03\x66\x61x\x18\x07 \x01(\x02\x12#\n\x05\x65xCfg\x18\x08 \x01(\x0b\x32\x14.google.protobuf.Any\"\x17\n\x15GeneralMessageRequest\"\x18\n\x16GeneralMessageResponse\"K\n\x0cGetHealthRsp\x12\x0b\n\x03\x63pu\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x0e\n\x06handle\x18\x03 \x01(\x05\x12\x0e\n\x06health\x18\x04 \x01(\t\"W\n\rGetVersionRsp\x12\x12\n\nserviceVer\x18\x01 \x01(\t\x12\x0e\n\x06gitVer\x18\x02 \x01(\t\x12\x11\n\tbuildDate\x18\x03 \x01(\t\x12\x0f\n\x07\x62uildIp\x18\x04 \x01(\t\"\x1a\n\x0bGetStackRsp\x12\x0b\n\x03\x62uf\x18\x01 \x01(\t\"+\n\rServiceCmdReq\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\r\n\x05param\x18\x02 \x01(\t\"\x1c\n\rServiceCmdRsp\x12\x0b\n\x03\x62uf\x18\x01 \x01(\t\"\'\n\x10\x42\x61kAndRestartReq\x12\x13\n\x0bserviceFlag\x18\x01 \x01(\t\"\x1f\n\x10\x42\x61kAndRestartRsp\x12\x0b\n\x03rsp\x18\x01 \x01(\x0c*\xb9\x01\n\x08GameType\x12\x0b\n\x07\x44\x65\x66\x61lut\x10\x00\x12\x07\n\x03\x44\x44Z\x10\x64\x12\x08\n\x04SHBY\x10\x65\x12\x08\n\x04QZNN\x10\x66\x12\x08\n\x04HHDZ\x10g\x12\x08\n\x04JDNN\x10h\x12\x08\n\x04\x42RNN\x10i\x12\x07\n\x03LHD\x10j\x12\x07\n\x03PDK\x10k\x12\x08\n\x04\x45RMJ\x10l\x12\x07\n\x03ZJH\x10m\x12\x08\n\x04\x44ZPK\x10n\x12\x08\n\x04HBSL\x10o\x12\x07\n\x03\x45\x42G\x10p\x12\x08\n\x04\x44\x46\x44\x43\x10q\x12\x08\n\x04\x45SYD\x10r\x12\x06\n\x02SG\x10s\x12\x07\n\x03SSS\x10t*(\n\x08RoomType\x12\x08\n\x04\x46ree\x10\x00\x12\x08\n\x04Take\x10\x01\x12\x08\n\x04Give\x10\x02\x32\\\n\x07Publics\x12Q\n\x0eGeneralMessage\x12\x1d.public.GeneralMessageRequest\x1a\x1e.public.GeneralMessageResponse\"\x00\x32\xc1\x02\n\x03\x43md\x12;\n\tGetHealth\x12\x16.google.protobuf.Empty\x1a\x14.public.GetHealthRsp\"\x00\x12=\n\nGetVersion\x12\x16.google.protobuf.Empty\x1a\x15.public.GetVersionRsp\"\x00\x12\x39\n\x08GetStack\x12\x16.google.protobuf.Empty\x1a\x13.public.GetStackRsp\"\x00\x12<\n\nServiceCmd\x12\x15.public.ServiceCmdReq\x1a\x15.public.ServiceCmdRsp\"\x00\x12\x45\n\rBakAndRestart\x12\x18.public.BakAndRestartReq\x1a\x18.public.BakAndRestartRsp\"\x00\x42$Z\"windplatform/server/protogo/publicb\x06proto3'
  ,
  dependencies=[any__pb2.DESCRIPTOR,empty__pb2.DESCRIPTOR,])

_GAMETYPE = _descriptor.EnumDescriptor(
  name='GameType',
  full_name='public.GameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Defalut', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DDZ', index=1, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHBY', index=2, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QZNN', index=3, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HHDZ', index=4, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JDNN', index=5, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRNN', index=6, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LHD', index=7, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PDK', index=8, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERMJ', index=9, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZJH', index=10, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DZPK', index=11, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HBSL', index=12, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EBG', index=13, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DFDC', index=14, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ESYD', index=15, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SG', index=16, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSS', index=17, number=116,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=801,
  serialized_end=986,
)
_sym_db.RegisterEnumDescriptor(_GAMETYPE)

GameType = enum_type_wrapper.EnumTypeWrapper(_GAMETYPE)
_ROOMTYPE = _descriptor.EnumDescriptor(
  name='RoomType',
  full_name='public.RoomType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Free', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Take', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Give', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=988,
  serialized_end=1028,
)
_sym_db.RegisterEnumDescriptor(_ROOMTYPE)

RoomType = enum_type_wrapper.EnumTypeWrapper(_ROOMTYPE)
Defalut = 0
DDZ = 100
SHBY = 101
QZNN = 102
HHDZ = 103
JDNN = 104
BRNN = 105
LHD = 106
PDK = 107
ERMJ = 108
ZJH = 109
DZPK = 110
HBSL = 111
EBG = 112
DFDC = 113
ESYD = 114
SG = 115
SSS = 116
Free = 0
Take = 1
Give = 2



_CLIENTDATA = _descriptor.Descriptor(
  name='ClientData',
  full_name='public.ClientData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerID', full_name='public.ClientData.playerID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gwName', full_name='public.ClientData.gwName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddr', full_name='public.ClientData.ipAddr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=48,
  serialized_end=110,
)


_PLAYERBASEINFO = _descriptor.Descriptor(
  name='PlayerBaseInfo',
  full_name='public.PlayerBaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerID', full_name='public.PlayerBaseInfo.playerID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='public.PlayerBaseInfo.nickName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='public.PlayerBaseInfo.avatar', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='public.PlayerBaseInfo.money', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seat', full_name='public.PlayerBaseInfo.seat', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=112,
  serialized_end=209,
)


_GAMECFG = _descriptor.Descriptor(
  name='GameCfg',
  full_name='public.GameCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kickTime', full_name='public.GameCfg.kickTime', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waitTimeBeforStart', full_name='public.GameCfg.waitTimeBeforStart', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minUserCnt', full_name='public.GameCfg.minUserCnt', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxUserCnt', full_name='public.GameCfg.maxUserCnt', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterLevelWin', full_name='public.GameCfg.waterLevelWin', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterLevelLose', full_name='public.GameCfg.waterLevelLose', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fax', full_name='public.GameCfg.fax', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exCfg', full_name='public.GameCfg.exCfg', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=212,
  serialized_end=404,
)


_GENERALMESSAGEREQUEST = _descriptor.Descriptor(
  name='GeneralMessageRequest',
  full_name='public.GeneralMessageRequest',
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
  serialized_start=406,
  serialized_end=429,
)


_GENERALMESSAGERESPONSE = _descriptor.Descriptor(
  name='GeneralMessageResponse',
  full_name='public.GeneralMessageResponse',
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
  serialized_start=431,
  serialized_end=455,
)


_GETHEALTHRSP = _descriptor.Descriptor(
  name='GetHealthRsp',
  full_name='public.GetHealthRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='public.GetHealthRsp.cpu', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='public.GetHealthRsp.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handle', full_name='public.GetHealthRsp.handle', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='public.GetHealthRsp.health', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=457,
  serialized_end=532,
)


_GETVERSIONRSP = _descriptor.Descriptor(
  name='GetVersionRsp',
  full_name='public.GetVersionRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceVer', full_name='public.GetVersionRsp.serviceVer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gitVer', full_name='public.GetVersionRsp.gitVer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buildDate', full_name='public.GetVersionRsp.buildDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buildIp', full_name='public.GetVersionRsp.buildIp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=534,
  serialized_end=621,
)


_GETSTACKRSP = _descriptor.Descriptor(
  name='GetStackRsp',
  full_name='public.GetStackRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buf', full_name='public.GetStackRsp.buf', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=623,
  serialized_end=649,
)


_SERVICECMDREQ = _descriptor.Descriptor(
  name='ServiceCmdReq',
  full_name='public.ServiceCmdReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='public.ServiceCmdReq.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='public.ServiceCmdReq.param', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=651,
  serialized_end=694,
)


_SERVICECMDRSP = _descriptor.Descriptor(
  name='ServiceCmdRsp',
  full_name='public.ServiceCmdRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buf', full_name='public.ServiceCmdRsp.buf', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=696,
  serialized_end=724,
)


_BAKANDRESTARTREQ = _descriptor.Descriptor(
  name='BakAndRestartReq',
  full_name='public.BakAndRestartReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceFlag', full_name='public.BakAndRestartReq.serviceFlag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=726,
  serialized_end=765,
)


_BAKANDRESTARTRSP = _descriptor.Descriptor(
  name='BakAndRestartRsp',
  full_name='public.BakAndRestartRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rsp', full_name='public.BakAndRestartRsp.rsp', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=767,
  serialized_end=798,
)

_GAMECFG.fields_by_name['exCfg'].message_type = any__pb2._ANY
DESCRIPTOR.message_types_by_name['ClientData'] = _CLIENTDATA
DESCRIPTOR.message_types_by_name['PlayerBaseInfo'] = _PLAYERBASEINFO
DESCRIPTOR.message_types_by_name['GameCfg'] = _GAMECFG
DESCRIPTOR.message_types_by_name['GeneralMessageRequest'] = _GENERALMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['GeneralMessageResponse'] = _GENERALMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['GetHealthRsp'] = _GETHEALTHRSP
DESCRIPTOR.message_types_by_name['GetVersionRsp'] = _GETVERSIONRSP
DESCRIPTOR.message_types_by_name['GetStackRsp'] = _GETSTACKRSP
DESCRIPTOR.message_types_by_name['ServiceCmdReq'] = _SERVICECMDREQ
DESCRIPTOR.message_types_by_name['ServiceCmdRsp'] = _SERVICECMDRSP
DESCRIPTOR.message_types_by_name['BakAndRestartReq'] = _BAKANDRESTARTREQ
DESCRIPTOR.message_types_by_name['BakAndRestartRsp'] = _BAKANDRESTARTRSP
DESCRIPTOR.enum_types_by_name['GameType'] = _GAMETYPE
DESCRIPTOR.enum_types_by_name['RoomType'] = _ROOMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientData = _reflection.GeneratedProtocolMessageType('ClientData', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTDATA,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.ClientData)
  })
_sym_db.RegisterMessage(ClientData)

PlayerBaseInfo = _reflection.GeneratedProtocolMessageType('PlayerBaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERBASEINFO,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.PlayerBaseInfo)
  })
_sym_db.RegisterMessage(PlayerBaseInfo)

GameCfg = _reflection.GeneratedProtocolMessageType('GameCfg', (_message.Message,), {
  'DESCRIPTOR' : _GAMECFG,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GameCfg)
  })
_sym_db.RegisterMessage(GameCfg)

GeneralMessageRequest = _reflection.GeneratedProtocolMessageType('GeneralMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERALMESSAGEREQUEST,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GeneralMessageRequest)
  })
_sym_db.RegisterMessage(GeneralMessageRequest)

GeneralMessageResponse = _reflection.GeneratedProtocolMessageType('GeneralMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERALMESSAGERESPONSE,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GeneralMessageResponse)
  })
_sym_db.RegisterMessage(GeneralMessageResponse)

GetHealthRsp = _reflection.GeneratedProtocolMessageType('GetHealthRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETHEALTHRSP,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GetHealthRsp)
  })
_sym_db.RegisterMessage(GetHealthRsp)

GetVersionRsp = _reflection.GeneratedProtocolMessageType('GetVersionRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONRSP,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GetVersionRsp)
  })
_sym_db.RegisterMessage(GetVersionRsp)

GetStackRsp = _reflection.GeneratedProtocolMessageType('GetStackRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETSTACKRSP,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.GetStackRsp)
  })
_sym_db.RegisterMessage(GetStackRsp)

ServiceCmdReq = _reflection.GeneratedProtocolMessageType('ServiceCmdReq', (_message.Message,), {
  'DESCRIPTOR' : _SERVICECMDREQ,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.ServiceCmdReq)
  })
_sym_db.RegisterMessage(ServiceCmdReq)

ServiceCmdRsp = _reflection.GeneratedProtocolMessageType('ServiceCmdRsp', (_message.Message,), {
  'DESCRIPTOR' : _SERVICECMDRSP,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.ServiceCmdRsp)
  })
_sym_db.RegisterMessage(ServiceCmdRsp)

BakAndRestartReq = _reflection.GeneratedProtocolMessageType('BakAndRestartReq', (_message.Message,), {
  'DESCRIPTOR' : _BAKANDRESTARTREQ,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.BakAndRestartReq)
  })
_sym_db.RegisterMessage(BakAndRestartReq)

BakAndRestartRsp = _reflection.GeneratedProtocolMessageType('BakAndRestartRsp', (_message.Message,), {
  'DESCRIPTOR' : _BAKANDRESTARTRSP,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.BakAndRestartRsp)
  })
_sym_db.RegisterMessage(BakAndRestartRsp)


DESCRIPTOR._options = None

_PUBLICS = _descriptor.ServiceDescriptor(
  name='Publics',
  full_name='public.Publics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1030,
  serialized_end=1122,
  methods=[
  _descriptor.MethodDescriptor(
    name='GeneralMessage',
    full_name='public.Publics.GeneralMessage',
    index=0,
    containing_service=None,
    input_type=_GENERALMESSAGEREQUEST,
    output_type=_GENERALMESSAGERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUBLICS)

DESCRIPTOR.services_by_name['Publics'] = _PUBLICS


_CMD = _descriptor.ServiceDescriptor(
  name='Cmd',
  full_name='public.Cmd',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1125,
  serialized_end=1446,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHealth',
    full_name='public.Cmd.GetHealth',
    index=0,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=_GETHEALTHRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='public.Cmd.GetVersion',
    index=1,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=_GETVERSIONRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStack',
    full_name='public.Cmd.GetStack',
    index=2,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=_GETSTACKRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServiceCmd',
    full_name='public.Cmd.ServiceCmd',
    index=3,
    containing_service=None,
    input_type=_SERVICECMDREQ,
    output_type=_SERVICECMDRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BakAndRestart',
    full_name='public.Cmd.BakAndRestart',
    index=4,
    containing_service=None,
    input_type=_BAKANDRESTARTREQ,
    output_type=_BAKANDRESTARTRSP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CMD)

DESCRIPTOR.services_by_name['Cmd'] = _CMD

# @@protoc_insertion_point(module_scope)
