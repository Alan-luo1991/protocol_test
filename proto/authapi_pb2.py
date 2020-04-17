# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authapi.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import empty_pb2 as empty__pb2
import agentbase_pb2 as agentbase__pb2
import attrinfo_pb2 as attrinfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='authapi.proto',
  package='auth.api',
  syntax='proto3',
  serialized_options=b'Z#windplatform/server/protogo/authapi',
  serialized_pb=b'\n\rauthapi.proto\x12\x08\x61uth.api\x1a\x0b\x65mpty.proto\x1a\x0f\x61gentbase.proto\x1a\x0e\x61ttrinfo.proto\"=\n\x11\x41gentTokenRequest\x12(\n\tagentInfo\x18\x01 \x01(\x0b\x32\x15.agent.base.AgentInfo\"@\n\x12\x41gentTokenResponse\x12*\n\nagentToken\x18\x01 \x01(\x0b\x32\x16.agent.base.AgentToken\"C\n\x17\x41gentTokenVerifyRequest\x12(\n\ttokenInfo\x18\x01 \x01(\x0b\x32\x15.agent.base.TokenInfo\"J\n\x18\x41gentTokenVerifyResponse\x12.\n\x0cverifyResult\x18\x01 \x01(\x0b\x32\x18.agent.base.VerifyResult\"w\n\x12PlayerTokenRequest\x12\x0f\n\x07\x61gentID\x18\x01 \x01(\t\x12\x0e\n\x06userID\x18\x02 \x01(\t\x12\x0e\n\x06ipAddr\x18\x03 \x01(\t\x12\x0c\n\x04lang\x18\x04 \x01(\t\x12\x10\n\x08platform\x18\x05 \x01(\t\x12\x10\n\x08userName\x18\x06 \x01(\t\"I\n\x13PlayerTokenResponse\x12\x10\n\x08playerID\x18\x01 \x01(\t\x12\x11\n\tlobbyAddr\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"3\n\x12VerifyTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06ipAddr\x18\x02 \x01(\t\"8\n\x13VerifyTokenResponse\x12\x10\n\x08playerID\x18\x01 \x01(\t\x12\x0f\n\x07\x61gentID\x18\x02 \x01(\t\"K\n\x15GetCustomerServiceReq\x12\x10\n\x08playerID\x18\x01 \x01(\t\x12\x12\n\nplayerName\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"0\n\x15GetCustomerServiceRsp\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\"6\n\x13\x43\x61ncelPlayerAuthReq\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x0f\n\x07\x61gentID\x18\x02 \x01(\t2\xf4\x03\n\x04\x41uth\x12I\n\nAgentToken\x12\x1b.auth.api.AgentTokenRequest\x1a\x1c.auth.api.AgentTokenResponse\"\x00\x12[\n\x10\x41gentTokenVerify\x12!.auth.api.AgentTokenVerifyRequest\x1a\".auth.api.AgentTokenVerifyResponse\"\x00\x12L\n\x0bPlayerToken\x12\x1c.auth.api.PlayerTokenRequest\x1a\x1d.auth.api.PlayerTokenResponse\"\x00\x12R\n\x11PlayerTokenVerify\x12\x1c.auth.api.VerifyTokenRequest\x1a\x1d.auth.api.VerifyTokenResponse\"\x00\x12U\n\x0f\x43ustomerService\x12\x1f.auth.api.GetCustomerServiceReq\x1a\x1f.auth.api.GetCustomerServiceRsp\"\x00\x12K\n\x10\x43\x61ncelPlayerAuth\x12\x1d.auth.api.CancelPlayerAuthReq\x1a\x16.google.protobuf.Empty\"\x00\x42%Z#windplatform/server/protogo/authapib\x06proto3'
  ,
  dependencies=[empty__pb2.DESCRIPTOR,agentbase__pb2.DESCRIPTOR,attrinfo__pb2.DESCRIPTOR,])




_AGENTTOKENREQUEST = _descriptor.Descriptor(
  name='AgentTokenRequest',
  full_name='auth.api.AgentTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentInfo', full_name='auth.api.AgentTokenRequest.agentInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=73,
  serialized_end=134,
)


_AGENTTOKENRESPONSE = _descriptor.Descriptor(
  name='AgentTokenResponse',
  full_name='auth.api.AgentTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentToken', full_name='auth.api.AgentTokenResponse.agentToken', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=136,
  serialized_end=200,
)


_AGENTTOKENVERIFYREQUEST = _descriptor.Descriptor(
  name='AgentTokenVerifyRequest',
  full_name='auth.api.AgentTokenVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokenInfo', full_name='auth.api.AgentTokenVerifyRequest.tokenInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=202,
  serialized_end=269,
)


_AGENTTOKENVERIFYRESPONSE = _descriptor.Descriptor(
  name='AgentTokenVerifyResponse',
  full_name='auth.api.AgentTokenVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verifyResult', full_name='auth.api.AgentTokenVerifyResponse.verifyResult', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=271,
  serialized_end=345,
)


_PLAYERTOKENREQUEST = _descriptor.Descriptor(
  name='PlayerTokenRequest',
  full_name='auth.api.PlayerTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentID', full_name='auth.api.PlayerTokenRequest.agentID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userID', full_name='auth.api.PlayerTokenRequest.userID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddr', full_name='auth.api.PlayerTokenRequest.ipAddr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='auth.api.PlayerTokenRequest.lang', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='auth.api.PlayerTokenRequest.platform', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='auth.api.PlayerTokenRequest.userName', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=347,
  serialized_end=466,
)


_PLAYERTOKENRESPONSE = _descriptor.Descriptor(
  name='PlayerTokenResponse',
  full_name='auth.api.PlayerTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerID', full_name='auth.api.PlayerTokenResponse.playerID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobbyAddr', full_name='auth.api.PlayerTokenResponse.lobbyAddr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='auth.api.PlayerTokenResponse.token', index=2,
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
  serialized_start=468,
  serialized_end=541,
)


_VERIFYTOKENREQUEST = _descriptor.Descriptor(
  name='VerifyTokenRequest',
  full_name='auth.api.VerifyTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='auth.api.VerifyTokenRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddr', full_name='auth.api.VerifyTokenRequest.ipAddr', index=1,
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
  serialized_start=543,
  serialized_end=594,
)


_VERIFYTOKENRESPONSE = _descriptor.Descriptor(
  name='VerifyTokenResponse',
  full_name='auth.api.VerifyTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerID', full_name='auth.api.VerifyTokenResponse.playerID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentID', full_name='auth.api.VerifyTokenResponse.agentID', index=1,
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
  serialized_start=596,
  serialized_end=652,
)


_GETCUSTOMERSERVICEREQ = _descriptor.Descriptor(
  name='GetCustomerServiceReq',
  full_name='auth.api.GetCustomerServiceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerID', full_name='auth.api.GetCustomerServiceReq.playerID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerName', full_name='auth.api.GetCustomerServiceReq.playerName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='auth.api.GetCustomerServiceReq.type', index=2,
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
  serialized_start=654,
  serialized_end=729,
)


_GETCUSTOMERSERVICERSP = _descriptor.Descriptor(
  name='GetCustomerServiceRsp',
  full_name='auth.api.GetCustomerServiceRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='auth.api.GetCustomerServiceRsp.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='auth.api.GetCustomerServiceRsp.ip', index=1,
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
  serialized_start=731,
  serialized_end=779,
)


_CANCELPLAYERAUTHREQ = _descriptor.Descriptor(
  name='CancelPlayerAuthReq',
  full_name='auth.api.CancelPlayerAuthReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='auth.api.CancelPlayerAuthReq.userID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentID', full_name='auth.api.CancelPlayerAuthReq.agentID', index=1,
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
  serialized_start=781,
  serialized_end=835,
)

_AGENTTOKENREQUEST.fields_by_name['agentInfo'].message_type = agentbase__pb2._AGENTINFO
_AGENTTOKENRESPONSE.fields_by_name['agentToken'].message_type = agentbase__pb2._AGENTTOKEN
_AGENTTOKENVERIFYREQUEST.fields_by_name['tokenInfo'].message_type = agentbase__pb2._TOKENINFO
_AGENTTOKENVERIFYRESPONSE.fields_by_name['verifyResult'].message_type = agentbase__pb2._VERIFYRESULT
DESCRIPTOR.message_types_by_name['AgentTokenRequest'] = _AGENTTOKENREQUEST
DESCRIPTOR.message_types_by_name['AgentTokenResponse'] = _AGENTTOKENRESPONSE
DESCRIPTOR.message_types_by_name['AgentTokenVerifyRequest'] = _AGENTTOKENVERIFYREQUEST
DESCRIPTOR.message_types_by_name['AgentTokenVerifyResponse'] = _AGENTTOKENVERIFYRESPONSE
DESCRIPTOR.message_types_by_name['PlayerTokenRequest'] = _PLAYERTOKENREQUEST
DESCRIPTOR.message_types_by_name['PlayerTokenResponse'] = _PLAYERTOKENRESPONSE
DESCRIPTOR.message_types_by_name['VerifyTokenRequest'] = _VERIFYTOKENREQUEST
DESCRIPTOR.message_types_by_name['VerifyTokenResponse'] = _VERIFYTOKENRESPONSE
DESCRIPTOR.message_types_by_name['GetCustomerServiceReq'] = _GETCUSTOMERSERVICEREQ
DESCRIPTOR.message_types_by_name['GetCustomerServiceRsp'] = _GETCUSTOMERSERVICERSP
DESCRIPTOR.message_types_by_name['CancelPlayerAuthReq'] = _CANCELPLAYERAUTHREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentTokenRequest = _reflection.GeneratedProtocolMessageType('AgentTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTOKENREQUEST,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.AgentTokenRequest)
  })
_sym_db.RegisterMessage(AgentTokenRequest)

AgentTokenResponse = _reflection.GeneratedProtocolMessageType('AgentTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTOKENRESPONSE,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.AgentTokenResponse)
  })
_sym_db.RegisterMessage(AgentTokenResponse)

AgentTokenVerifyRequest = _reflection.GeneratedProtocolMessageType('AgentTokenVerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTOKENVERIFYREQUEST,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.AgentTokenVerifyRequest)
  })
_sym_db.RegisterMessage(AgentTokenVerifyRequest)

AgentTokenVerifyResponse = _reflection.GeneratedProtocolMessageType('AgentTokenVerifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTOKENVERIFYRESPONSE,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.AgentTokenVerifyResponse)
  })
_sym_db.RegisterMessage(AgentTokenVerifyResponse)

PlayerTokenRequest = _reflection.GeneratedProtocolMessageType('PlayerTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERTOKENREQUEST,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.PlayerTokenRequest)
  })
_sym_db.RegisterMessage(PlayerTokenRequest)

PlayerTokenResponse = _reflection.GeneratedProtocolMessageType('PlayerTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERTOKENRESPONSE,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.PlayerTokenResponse)
  })
_sym_db.RegisterMessage(PlayerTokenResponse)

VerifyTokenRequest = _reflection.GeneratedProtocolMessageType('VerifyTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENREQUEST,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.VerifyTokenRequest)
  })
_sym_db.RegisterMessage(VerifyTokenRequest)

VerifyTokenResponse = _reflection.GeneratedProtocolMessageType('VerifyTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENRESPONSE,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.VerifyTokenResponse)
  })
_sym_db.RegisterMessage(VerifyTokenResponse)

GetCustomerServiceReq = _reflection.GeneratedProtocolMessageType('GetCustomerServiceReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERSERVICEREQ,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.GetCustomerServiceReq)
  })
_sym_db.RegisterMessage(GetCustomerServiceReq)

GetCustomerServiceRsp = _reflection.GeneratedProtocolMessageType('GetCustomerServiceRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERSERVICERSP,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.GetCustomerServiceRsp)
  })
_sym_db.RegisterMessage(GetCustomerServiceRsp)

CancelPlayerAuthReq = _reflection.GeneratedProtocolMessageType('CancelPlayerAuthReq', (_message.Message,), {
  'DESCRIPTOR' : _CANCELPLAYERAUTHREQ,
  '__module__' : 'authapi_pb2'
  # @@protoc_insertion_point(class_scope:auth.api.CancelPlayerAuthReq)
  })
_sym_db.RegisterMessage(CancelPlayerAuthReq)


DESCRIPTOR._options = None

_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='auth.api.Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=838,
  serialized_end=1338,
  methods=[
  _descriptor.MethodDescriptor(
    name='AgentToken',
    full_name='auth.api.Auth.AgentToken',
    index=0,
    containing_service=None,
    input_type=_AGENTTOKENREQUEST,
    output_type=_AGENTTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AgentTokenVerify',
    full_name='auth.api.Auth.AgentTokenVerify',
    index=1,
    containing_service=None,
    input_type=_AGENTTOKENVERIFYREQUEST,
    output_type=_AGENTTOKENVERIFYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PlayerToken',
    full_name='auth.api.Auth.PlayerToken',
    index=2,
    containing_service=None,
    input_type=_PLAYERTOKENREQUEST,
    output_type=_PLAYERTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PlayerTokenVerify',
    full_name='auth.api.Auth.PlayerTokenVerify',
    index=3,
    containing_service=None,
    input_type=_VERIFYTOKENREQUEST,
    output_type=_VERIFYTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CustomerService',
    full_name='auth.api.Auth.CustomerService',
    index=4,
    containing_service=None,
    input_type=_GETCUSTOMERSERVICEREQ,
    output_type=_GETCUSTOMERSERVICERSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelPlayerAuth',
    full_name='auth.api.Auth.CancelPlayerAuth',
    index=5,
    containing_service=None,
    input_type=_CANCELPLAYERAUTHREQ,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)