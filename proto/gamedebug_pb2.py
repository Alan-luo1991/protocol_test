# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamedebug.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamedebug.proto',
  package='game.debug',
  syntax='proto3',
  serialized_options=b'Z%windplatform/server/protogo/gamedebug',
  serialized_pb=b'\n\x0fgamedebug.proto\x12\ngame.debug\"\xa0\x03\n\x06Player\x12\x10\n\x08playerId\x18\x01 \x01(\t\x12\x0c\n\x04seat\x18\x02 \x01(\x05\x12\x10\n\x08\x61vatarId\x18\x03 \x01(\x05\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x10\n\x08\x62odyType\x18\x06 \x01(\t\x12\x11\n\tleaveType\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12+\n\tmoneyInfo\x18\t \x01(\x0b\x32\x18.game.debug.Player.money\x12\x13\n\x0b\x65nableRobot\x18\n \x01(\t\x12\x10\n\x08\x65nableIp\x18\x0b \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\x1a\xb1\x01\n\x05money\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x03\x12\x11\n\tscoreFlow\x18\x02 \x01(\x03\x12\x0f\n\x07winLose\x18\x03 \x01(\x03\x12\x12\n\nvisibleTax\x18\x04 \x01(\x03\x12\x14\n\x0cinvisibleTax\x18\x05 \x01(\x03\x12\x10\n\x08\x63trlType\x18\x06 \x01(\t\x12\x10\n\x08killRate\x18\x07 \x01(\x02\x12\x10\n\x08gameData\x18\x08 \x01(\t\x12\x13\n\x0bkindWinLose\x18\n \x01(\x03\"\x93\x01\n\x04Room\x12\x0e\n\x06roomId\x18\x01 \x01(\t\x12\x0e\n\x06kindId\x18\x02 \x01(\r\x12\x0f\n\x07roundId\x18\x03 \x01(\t\x12\x0e\n\x06roomIp\x18\x04 \x01(\t\x12\x12\n\nroundCount\x18\x05 \x01(\x05\x12\x11\n\tgameState\x18\x06 \x01(\t\x12#\n\x07players\x18\x07 \x03(\x0b\x32\x12.game.debug.Player\"\xd5\x02\n\x0eGetRoomListRsp\x12\x36\n\x06\x61gents\x18\x02 \x03(\x0b\x32&.game.debug.GetRoomListRsp.AgentsEntry\x1a\'\n\x05Rooms\x12\x1e\n\x04room\x18\x01 \x03(\x0b\x32\x10.game.debug.Room\x1a\x91\x01\n\x04Kind\x12\x39\n\x05kinds\x18\x01 \x03(\x0b\x32*.game.debug.GetRoomListRsp.Kind.KindsEntry\x1aN\n\nKindsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .game.debug.GetRoomListRsp.Rooms:\x02\x38\x01\x1aN\n\x0b\x41gentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.game.debug.GetRoomListRsp.Kind:\x02\x38\x01\" \n\x0cGetPlayerReq\x12\x10\n\x08playerId\x18\x01 \x01(\t\"r\n\rGetSummaryRsp\x12\x16\n\x0etotalRoomCount\x18\x01 \x01(\x05\x12\x16\n\x0erobotRoomCount\x18\x02 \x01(\x05\x12\x18\n\x10totalPlayerCount\x18\x03 \x01(\x05\x12\x17\n\x0frealPlayerCount\x18\x04 \x01(\x05\x42\'Z%windplatform/server/protogo/gamedebugb\x06proto3'
)




_PLAYER_MONEY = _descriptor.Descriptor(
  name='money',
  full_name='game.debug.Player.money',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='game.debug.Player.money.balance', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scoreFlow', full_name='game.debug.Player.money.scoreFlow', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='winLose', full_name='game.debug.Player.money.winLose', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibleTax', full_name='game.debug.Player.money.visibleTax', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invisibleTax', full_name='game.debug.Player.money.invisibleTax', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctrlType', full_name='game.debug.Player.money.ctrlType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='killRate', full_name='game.debug.Player.money.killRate', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameData', full_name='game.debug.Player.money.gameData', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kindWinLose', full_name='game.debug.Player.money.kindWinLose', index=8,
      number=10, type=3, cpp_type=2, label=1,
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
  serialized_start=271,
  serialized_end=448,
)

_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='game.debug.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='game.debug.Player.playerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seat', full_name='game.debug.Player.seat', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatarId', full_name='game.debug.Player.avatarId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='game.debug.Player.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region', full_name='game.debug.Player.region', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bodyType', full_name='game.debug.Player.bodyType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leaveType', full_name='game.debug.Player.leaveType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='game.debug.Player.state', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moneyInfo', full_name='game.debug.Player.moneyInfo', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableRobot', full_name='game.debug.Player.enableRobot', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableIp', full_name='game.debug.Player.enableIp', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='game.debug.Player.name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PLAYER_MONEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=448,
)


_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='game.debug.Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomId', full_name='game.debug.Room.roomId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kindId', full_name='game.debug.Room.kindId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roundId', full_name='game.debug.Room.roundId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomIp', full_name='game.debug.Room.roomIp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roundCount', full_name='game.debug.Room.roundCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameState', full_name='game.debug.Room.gameState', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='game.debug.Room.players', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=451,
  serialized_end=598,
)


_GETROOMLISTRSP_ROOMS = _descriptor.Descriptor(
  name='Rooms',
  full_name='game.debug.GetRoomListRsp.Rooms',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room', full_name='game.debug.GetRoomListRsp.Rooms.room', index=0,
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
  serialized_start=675,
  serialized_end=714,
)

_GETROOMLISTRSP_KIND_KINDSENTRY = _descriptor.Descriptor(
  name='KindsEntry',
  full_name='game.debug.GetRoomListRsp.Kind.KindsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='game.debug.GetRoomListRsp.Kind.KindsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='game.debug.GetRoomListRsp.Kind.KindsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=862,
)

_GETROOMLISTRSP_KIND = _descriptor.Descriptor(
  name='Kind',
  full_name='game.debug.GetRoomListRsp.Kind',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kinds', full_name='game.debug.GetRoomListRsp.Kind.kinds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETROOMLISTRSP_KIND_KINDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=862,
)

_GETROOMLISTRSP_AGENTSENTRY = _descriptor.Descriptor(
  name='AgentsEntry',
  full_name='game.debug.GetRoomListRsp.AgentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='game.debug.GetRoomListRsp.AgentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='game.debug.GetRoomListRsp.AgentsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=942,
)

_GETROOMLISTRSP = _descriptor.Descriptor(
  name='GetRoomListRsp',
  full_name='game.debug.GetRoomListRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='game.debug.GetRoomListRsp.agents', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETROOMLISTRSP_ROOMS, _GETROOMLISTRSP_KIND, _GETROOMLISTRSP_AGENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=942,
)


_GETPLAYERREQ = _descriptor.Descriptor(
  name='GetPlayerReq',
  full_name='game.debug.GetPlayerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='game.debug.GetPlayerReq.playerId', index=0,
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
  serialized_start=944,
  serialized_end=976,
)


_GETSUMMARYRSP = _descriptor.Descriptor(
  name='GetSummaryRsp',
  full_name='game.debug.GetSummaryRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalRoomCount', full_name='game.debug.GetSummaryRsp.totalRoomCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robotRoomCount', full_name='game.debug.GetSummaryRsp.robotRoomCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalPlayerCount', full_name='game.debug.GetSummaryRsp.totalPlayerCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='realPlayerCount', full_name='game.debug.GetSummaryRsp.realPlayerCount', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=978,
  serialized_end=1092,
)

_PLAYER_MONEY.containing_type = _PLAYER
_PLAYER.fields_by_name['moneyInfo'].message_type = _PLAYER_MONEY
_ROOM.fields_by_name['players'].message_type = _PLAYER
_GETROOMLISTRSP_ROOMS.fields_by_name['room'].message_type = _ROOM
_GETROOMLISTRSP_ROOMS.containing_type = _GETROOMLISTRSP
_GETROOMLISTRSP_KIND_KINDSENTRY.fields_by_name['value'].message_type = _GETROOMLISTRSP_ROOMS
_GETROOMLISTRSP_KIND_KINDSENTRY.containing_type = _GETROOMLISTRSP_KIND
_GETROOMLISTRSP_KIND.fields_by_name['kinds'].message_type = _GETROOMLISTRSP_KIND_KINDSENTRY
_GETROOMLISTRSP_KIND.containing_type = _GETROOMLISTRSP
_GETROOMLISTRSP_AGENTSENTRY.fields_by_name['value'].message_type = _GETROOMLISTRSP_KIND
_GETROOMLISTRSP_AGENTSENTRY.containing_type = _GETROOMLISTRSP
_GETROOMLISTRSP.fields_by_name['agents'].message_type = _GETROOMLISTRSP_AGENTSENTRY
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['Room'] = _ROOM
DESCRIPTOR.message_types_by_name['GetRoomListRsp'] = _GETROOMLISTRSP
DESCRIPTOR.message_types_by_name['GetPlayerReq'] = _GETPLAYERREQ
DESCRIPTOR.message_types_by_name['GetSummaryRsp'] = _GETSUMMARYRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {

  'money' : _reflection.GeneratedProtocolMessageType('money', (_message.Message,), {
    'DESCRIPTOR' : _PLAYER_MONEY,
    '__module__' : 'gamedebug_pb2'
    # @@protoc_insertion_point(class_scope:game.debug.Player.money)
    })
  ,
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'gamedebug_pb2'
  # @@protoc_insertion_point(class_scope:game.debug.Player)
  })
_sym_db.RegisterMessage(Player)
_sym_db.RegisterMessage(Player.money)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), {
  'DESCRIPTOR' : _ROOM,
  '__module__' : 'gamedebug_pb2'
  # @@protoc_insertion_point(class_scope:game.debug.Room)
  })
_sym_db.RegisterMessage(Room)

GetRoomListRsp = _reflection.GeneratedProtocolMessageType('GetRoomListRsp', (_message.Message,), {

  'Rooms' : _reflection.GeneratedProtocolMessageType('Rooms', (_message.Message,), {
    'DESCRIPTOR' : _GETROOMLISTRSP_ROOMS,
    '__module__' : 'gamedebug_pb2'
    # @@protoc_insertion_point(class_scope:game.debug.GetRoomListRsp.Rooms)
    })
  ,

  'Kind' : _reflection.GeneratedProtocolMessageType('Kind', (_message.Message,), {

    'KindsEntry' : _reflection.GeneratedProtocolMessageType('KindsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETROOMLISTRSP_KIND_KINDSENTRY,
      '__module__' : 'gamedebug_pb2'
      # @@protoc_insertion_point(class_scope:game.debug.GetRoomListRsp.Kind.KindsEntry)
      })
    ,
    'DESCRIPTOR' : _GETROOMLISTRSP_KIND,
    '__module__' : 'gamedebug_pb2'
    # @@protoc_insertion_point(class_scope:game.debug.GetRoomListRsp.Kind)
    })
  ,

  'AgentsEntry' : _reflection.GeneratedProtocolMessageType('AgentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETROOMLISTRSP_AGENTSENTRY,
    '__module__' : 'gamedebug_pb2'
    # @@protoc_insertion_point(class_scope:game.debug.GetRoomListRsp.AgentsEntry)
    })
  ,
  'DESCRIPTOR' : _GETROOMLISTRSP,
  '__module__' : 'gamedebug_pb2'
  # @@protoc_insertion_point(class_scope:game.debug.GetRoomListRsp)
  })
_sym_db.RegisterMessage(GetRoomListRsp)
_sym_db.RegisterMessage(GetRoomListRsp.Rooms)
_sym_db.RegisterMessage(GetRoomListRsp.Kind)
_sym_db.RegisterMessage(GetRoomListRsp.Kind.KindsEntry)
_sym_db.RegisterMessage(GetRoomListRsp.AgentsEntry)

GetPlayerReq = _reflection.GeneratedProtocolMessageType('GetPlayerReq', (_message.Message,), {
  'DESCRIPTOR' : _GETPLAYERREQ,
  '__module__' : 'gamedebug_pb2'
  # @@protoc_insertion_point(class_scope:game.debug.GetPlayerReq)
  })
_sym_db.RegisterMessage(GetPlayerReq)

GetSummaryRsp = _reflection.GeneratedProtocolMessageType('GetSummaryRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETSUMMARYRSP,
  '__module__' : 'gamedebug_pb2'
  # @@protoc_insertion_point(class_scope:game.debug.GetSummaryRsp)
  })
_sym_db.RegisterMessage(GetSummaryRsp)


DESCRIPTOR._options = None
_GETROOMLISTRSP_KIND_KINDSENTRY._options = None
_GETROOMLISTRSP_AGENTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
