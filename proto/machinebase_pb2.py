# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinebase.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinebase.proto',
  package='machine.base',
  syntax='proto3',
  serialized_options=b'Z\'windplatform/server/protogo/machinebase',
  serialized_pb=b'\n\x11machinebase.proto\x12\x0cmachine.base\"^\n\nRunMsgInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x63puUse\x18\x02 \x03(\t\x12\x11\n\tmemoryUse\x18\x03 \x03(\t\x12\x0f\n\x07\x64iskUse\x18\x04 \x03(\t\x12\x0e\n\x06netUse\x18\x05 \x03(\t\"s\n\x0bHardMsgInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63puCapacity\x18\x02 \x01(\x05\x12\x16\n\x0ememoryCapacity\x18\x03 \x01(\x05\x12\x14\n\x0c\x64iskCapacity\x18\x04 \x01(\x05\x12\x13\n\x0bnetCapacity\x18\x05 \x01(\x05\",\n\x0bRoutingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x05\x42)Z\'windplatform/server/protogo/machinebaseb\x06proto3'
)




_RUNMSGINFO = _descriptor.Descriptor(
  name='RunMsgInfo',
  full_name='machine.base.RunMsgInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='machine.base.RunMsgInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpuUse', full_name='machine.base.RunMsgInfo.cpuUse', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memoryUse', full_name='machine.base.RunMsgInfo.memoryUse', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diskUse', full_name='machine.base.RunMsgInfo.diskUse', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netUse', full_name='machine.base.RunMsgInfo.netUse', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=35,
  serialized_end=129,
)


_HARDMSGINFO = _descriptor.Descriptor(
  name='HardMsgInfo',
  full_name='machine.base.HardMsgInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='machine.base.HardMsgInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpuCapacity', full_name='machine.base.HardMsgInfo.cpuCapacity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memoryCapacity', full_name='machine.base.HardMsgInfo.memoryCapacity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diskCapacity', full_name='machine.base.HardMsgInfo.diskCapacity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netCapacity', full_name='machine.base.HardMsgInfo.netCapacity', index=4,
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
  serialized_start=131,
  serialized_end=246,
)


_ROUTINGINFO = _descriptor.Descriptor(
  name='RoutingInfo',
  full_name='machine.base.RoutingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='machine.base.RoutingInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='machine.base.RoutingInfo.success', index=1,
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
  serialized_start=248,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['RunMsgInfo'] = _RUNMSGINFO
DESCRIPTOR.message_types_by_name['HardMsgInfo'] = _HARDMSGINFO
DESCRIPTOR.message_types_by_name['RoutingInfo'] = _ROUTINGINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunMsgInfo = _reflection.GeneratedProtocolMessageType('RunMsgInfo', (_message.Message,), {
  'DESCRIPTOR' : _RUNMSGINFO,
  '__module__' : 'machinebase_pb2'
  # @@protoc_insertion_point(class_scope:machine.base.RunMsgInfo)
  })
_sym_db.RegisterMessage(RunMsgInfo)

HardMsgInfo = _reflection.GeneratedProtocolMessageType('HardMsgInfo', (_message.Message,), {
  'DESCRIPTOR' : _HARDMSGINFO,
  '__module__' : 'machinebase_pb2'
  # @@protoc_insertion_point(class_scope:machine.base.HardMsgInfo)
  })
_sym_db.RegisterMessage(HardMsgInfo)

RoutingInfo = _reflection.GeneratedProtocolMessageType('RoutingInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGINFO,
  '__module__' : 'machinebase_pb2'
  # @@protoc_insertion_point(class_scope:machine.base.RoutingInfo)
  })
_sym_db.RegisterMessage(RoutingInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
