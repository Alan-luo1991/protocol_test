# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamecard.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamecard.proto',
  package='game.card',
  syntax='proto3',
  serialized_options=b'Z$windplatform/server/protogo/gamecard',
  serialized_pb=b'\n\x0egamecard.proto\x12\tgame.card\"t\n\x04\x43\x61rd\x12\r\n\x05point\x18\x01 \x01(\x05\x12&\n\x06\x66lower\x18\x02 \x01(\x0e\x32\x16.game.card.Card.Flower\"5\n\x06\x46lower\x12\x0b\n\x07\x44iamond\x10\x00\x12\x08\n\x04Plum\x10\x01\x12\t\n\x05Heart\x10\x02\x12\t\n\x05Spade\x10\x03\x42&Z$windplatform/server/protogo/gamecardb\x06proto3'
)



_CARD_FLOWER = _descriptor.EnumDescriptor(
  name='Flower',
  full_name='game.card.Card.Flower',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Diamond', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Plum', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Heart', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spade', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=92,
  serialized_end=145,
)
_sym_db.RegisterEnumDescriptor(_CARD_FLOWER)


_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='game.card.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='game.card.Card.point', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flower', full_name='game.card.Card.flower', index=1,
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
    _CARD_FLOWER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=145,
)

_CARD.fields_by_name['flower'].enum_type = _CARD_FLOWER
_CARD_FLOWER.containing_type = _CARD
DESCRIPTOR.message_types_by_name['Card'] = _CARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
  'DESCRIPTOR' : _CARD,
  '__module__' : 'gamecard_pb2'
  # @@protoc_insertion_point(class_scope:game.card.Card)
  })
_sym_db.RegisterMessage(Card)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)