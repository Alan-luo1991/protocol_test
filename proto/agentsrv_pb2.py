# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agentsrv.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import agentbase_pb2 as agentbase__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='agentsrv.proto',
  package='agent.srv',
  syntax='proto3',
  serialized_options=b'Z$windplatform/server/protogo/agentsrv',
  serialized_pb=b'\n\x0e\x61gentsrv.proto\x12\tagent.srv\x1a\x0f\x61gentbase.proto\">\n\x12VerifyAgentRequest\x12(\n\tagentInfo\x18\x01 \x01(\x0b\x32\x15.agent.base.AgentInfo\"A\n\x13VerifyAgentResponse\x12*\n\nagentToken\x18\x01 \x01(\x0b\x32\x16.agent.base.AgentToken\">\n\x12VerifyTokenRequest\x12(\n\ttokenInfo\x18\x01 \x01(\x0b\x32\x15.agent.base.TokenInfo\"E\n\x13VerifyTokenResponse\x12.\n\x0cverifyResult\x18\x01 \x01(\x0b\x32\x18.agent.base.VerifyResult\"\'\n\x14UpperScoreURLRequest\x12\x0f\n\x07\x61gentID\x18\x01 \x01(\t\"D\n\x15UpperScoreURLResponse\x12\x14\n\x0cscoreInfoURL\x18\x01 \x01(\t\x12\x15\n\rupperScoreURL\x18\x02 \x01(\t\"%\n\x12UpdateAgentRequest\x12\x0f\n\x07\x61gentID\x18\x01 \x01(\t\"%\n\x13UpdateAgentResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"&\n\x13GetOtherInfoRequest\x12\x0f\n\x07\x61gentID\x18\x01 \x01(\t\";\n\x14GetOtherInfoResponse\x12\x11\n\tEnablePay\x18\x01 \x01(\x08\x12\x10\n\x08\x45nableCs\x18\x02 \x01(\x08\"9\n\x14GetAllAddressRequest\x12\x0f\n\x07\x61gentID\x18\x01 \x01(\t\x12\x10\n\x08vipLevel\x18\x02 \x01(\r\"K\n\x15GetAllAddressResponse\x12\x0f\n\x07vipAddr\x18\x01 \x01(\t\x12\x0e\n\x06pcAddr\x18\x02 \x01(\t\x12\x11\n\tmobieAddr\x18\x03 \x01(\t\"&\n\x16GetSettlementMethodRsp\x12\x0c\n\x04mode\x18\x01 \x01(\r\" \n\x0fGetGiftMoneyRsp\x12\r\n\x05total\x18\x01 \x01(\x03\x32\x9f\x05\n\x0c\x41gentManager\x12N\n\x0bVerifyAgent\x12\x1d.agent.srv.VerifyAgentRequest\x1a\x1e.agent.srv.VerifyAgentResponse\"\x00\x12N\n\x0bVerifyToken\x12\x1d.agent.srv.VerifyTokenRequest\x1a\x1e.agent.srv.VerifyTokenResponse\"\x00\x12T\n\rUpperScoreURL\x12\x1f.agent.srv.UpperScoreURLRequest\x1a .agent.srv.UpperScoreURLResponse\"\x00\x12N\n\x0bUpdateAgent\x12\x1d.agent.srv.UpdateAgentRequest\x1a\x1e.agent.srv.UpdateAgentResponse\"\x00\x12O\n\x0cGetOtherInfo\x12\x1e.agent.srv.GetOtherInfoRequest\x1a\x1f.agent.srv.GetOtherInfoResponse\x12R\n\rGetAllAddress\x12\x1f.agent.srv.GetAllAddressRequest\x1a .agent.srv.GetAllAddressResponse\x12X\n\x13GetSettlementMethod\x12\x1e.agent.srv.GetOtherInfoRequest\x1a!.agent.srv.GetSettlementMethodRsp\x12J\n\x0cGetGiftMoney\x12\x1e.agent.srv.GetOtherInfoRequest\x1a\x1a.agent.srv.GetGiftMoneyRspB&Z$windplatform/server/protogo/agentsrvb\x06proto3'
  ,
  dependencies=[agentbase__pb2.DESCRIPTOR,])




_VERIFYAGENTREQUEST = _descriptor.Descriptor(
  name='VerifyAgentRequest',
  full_name='agent.srv.VerifyAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentInfo', full_name='agent.srv.VerifyAgentRequest.agentInfo', index=0,
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
  serialized_start=46,
  serialized_end=108,
)


_VERIFYAGENTRESPONSE = _descriptor.Descriptor(
  name='VerifyAgentResponse',
  full_name='agent.srv.VerifyAgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentToken', full_name='agent.srv.VerifyAgentResponse.agentToken', index=0,
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
  serialized_start=110,
  serialized_end=175,
)


_VERIFYTOKENREQUEST = _descriptor.Descriptor(
  name='VerifyTokenRequest',
  full_name='agent.srv.VerifyTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokenInfo', full_name='agent.srv.VerifyTokenRequest.tokenInfo', index=0,
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
  serialized_start=177,
  serialized_end=239,
)


_VERIFYTOKENRESPONSE = _descriptor.Descriptor(
  name='VerifyTokenResponse',
  full_name='agent.srv.VerifyTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verifyResult', full_name='agent.srv.VerifyTokenResponse.verifyResult', index=0,
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
  serialized_start=241,
  serialized_end=310,
)


_UPPERSCOREURLREQUEST = _descriptor.Descriptor(
  name='UpperScoreURLRequest',
  full_name='agent.srv.UpperScoreURLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentID', full_name='agent.srv.UpperScoreURLRequest.agentID', index=0,
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
  serialized_start=312,
  serialized_end=351,
)


_UPPERSCOREURLRESPONSE = _descriptor.Descriptor(
  name='UpperScoreURLResponse',
  full_name='agent.srv.UpperScoreURLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scoreInfoURL', full_name='agent.srv.UpperScoreURLResponse.scoreInfoURL', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upperScoreURL', full_name='agent.srv.UpperScoreURLResponse.upperScoreURL', index=1,
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
  serialized_start=353,
  serialized_end=421,
)


_UPDATEAGENTREQUEST = _descriptor.Descriptor(
  name='UpdateAgentRequest',
  full_name='agent.srv.UpdateAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentID', full_name='agent.srv.UpdateAgentRequest.agentID', index=0,
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
  serialized_start=423,
  serialized_end=460,
)


_UPDATEAGENTRESPONSE = _descriptor.Descriptor(
  name='UpdateAgentResponse',
  full_name='agent.srv.UpdateAgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='agent.srv.UpdateAgentResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=462,
  serialized_end=499,
)


_GETOTHERINFOREQUEST = _descriptor.Descriptor(
  name='GetOtherInfoRequest',
  full_name='agent.srv.GetOtherInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentID', full_name='agent.srv.GetOtherInfoRequest.agentID', index=0,
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
  serialized_start=501,
  serialized_end=539,
)


_GETOTHERINFORESPONSE = _descriptor.Descriptor(
  name='GetOtherInfoResponse',
  full_name='agent.srv.GetOtherInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EnablePay', full_name='agent.srv.GetOtherInfoResponse.EnablePay', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EnableCs', full_name='agent.srv.GetOtherInfoResponse.EnableCs', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=541,
  serialized_end=600,
)


_GETALLADDRESSREQUEST = _descriptor.Descriptor(
  name='GetAllAddressRequest',
  full_name='agent.srv.GetAllAddressRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentID', full_name='agent.srv.GetAllAddressRequest.agentID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vipLevel', full_name='agent.srv.GetAllAddressRequest.vipLevel', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=602,
  serialized_end=659,
)


_GETALLADDRESSRESPONSE = _descriptor.Descriptor(
  name='GetAllAddressResponse',
  full_name='agent.srv.GetAllAddressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vipAddr', full_name='agent.srv.GetAllAddressResponse.vipAddr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pcAddr', full_name='agent.srv.GetAllAddressResponse.pcAddr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobieAddr', full_name='agent.srv.GetAllAddressResponse.mobieAddr', index=2,
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
  serialized_start=661,
  serialized_end=736,
)


_GETSETTLEMENTMETHODRSP = _descriptor.Descriptor(
  name='GetSettlementMethodRsp',
  full_name='agent.srv.GetSettlementMethodRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='agent.srv.GetSettlementMethodRsp.mode', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=738,
  serialized_end=776,
)


_GETGIFTMONEYRSP = _descriptor.Descriptor(
  name='GetGiftMoneyRsp',
  full_name='agent.srv.GetGiftMoneyRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='agent.srv.GetGiftMoneyRsp.total', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=778,
  serialized_end=810,
)

_VERIFYAGENTREQUEST.fields_by_name['agentInfo'].message_type = agentbase__pb2._AGENTINFO
_VERIFYAGENTRESPONSE.fields_by_name['agentToken'].message_type = agentbase__pb2._AGENTTOKEN
_VERIFYTOKENREQUEST.fields_by_name['tokenInfo'].message_type = agentbase__pb2._TOKENINFO
_VERIFYTOKENRESPONSE.fields_by_name['verifyResult'].message_type = agentbase__pb2._VERIFYRESULT
DESCRIPTOR.message_types_by_name['VerifyAgentRequest'] = _VERIFYAGENTREQUEST
DESCRIPTOR.message_types_by_name['VerifyAgentResponse'] = _VERIFYAGENTRESPONSE
DESCRIPTOR.message_types_by_name['VerifyTokenRequest'] = _VERIFYTOKENREQUEST
DESCRIPTOR.message_types_by_name['VerifyTokenResponse'] = _VERIFYTOKENRESPONSE
DESCRIPTOR.message_types_by_name['UpperScoreURLRequest'] = _UPPERSCOREURLREQUEST
DESCRIPTOR.message_types_by_name['UpperScoreURLResponse'] = _UPPERSCOREURLRESPONSE
DESCRIPTOR.message_types_by_name['UpdateAgentRequest'] = _UPDATEAGENTREQUEST
DESCRIPTOR.message_types_by_name['UpdateAgentResponse'] = _UPDATEAGENTRESPONSE
DESCRIPTOR.message_types_by_name['GetOtherInfoRequest'] = _GETOTHERINFOREQUEST
DESCRIPTOR.message_types_by_name['GetOtherInfoResponse'] = _GETOTHERINFORESPONSE
DESCRIPTOR.message_types_by_name['GetAllAddressRequest'] = _GETALLADDRESSREQUEST
DESCRIPTOR.message_types_by_name['GetAllAddressResponse'] = _GETALLADDRESSRESPONSE
DESCRIPTOR.message_types_by_name['GetSettlementMethodRsp'] = _GETSETTLEMENTMETHODRSP
DESCRIPTOR.message_types_by_name['GetGiftMoneyRsp'] = _GETGIFTMONEYRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VerifyAgentRequest = _reflection.GeneratedProtocolMessageType('VerifyAgentRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYAGENTREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.VerifyAgentRequest)
  })
_sym_db.RegisterMessage(VerifyAgentRequest)

VerifyAgentResponse = _reflection.GeneratedProtocolMessageType('VerifyAgentResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYAGENTRESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.VerifyAgentResponse)
  })
_sym_db.RegisterMessage(VerifyAgentResponse)

VerifyTokenRequest = _reflection.GeneratedProtocolMessageType('VerifyTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.VerifyTokenRequest)
  })
_sym_db.RegisterMessage(VerifyTokenRequest)

VerifyTokenResponse = _reflection.GeneratedProtocolMessageType('VerifyTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENRESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.VerifyTokenResponse)
  })
_sym_db.RegisterMessage(VerifyTokenResponse)

UpperScoreURLRequest = _reflection.GeneratedProtocolMessageType('UpperScoreURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPPERSCOREURLREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.UpperScoreURLRequest)
  })
_sym_db.RegisterMessage(UpperScoreURLRequest)

UpperScoreURLResponse = _reflection.GeneratedProtocolMessageType('UpperScoreURLResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPPERSCOREURLRESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.UpperScoreURLResponse)
  })
_sym_db.RegisterMessage(UpperScoreURLResponse)

UpdateAgentRequest = _reflection.GeneratedProtocolMessageType('UpdateAgentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAGENTREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.UpdateAgentRequest)
  })
_sym_db.RegisterMessage(UpdateAgentRequest)

UpdateAgentResponse = _reflection.GeneratedProtocolMessageType('UpdateAgentResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAGENTRESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.UpdateAgentResponse)
  })
_sym_db.RegisterMessage(UpdateAgentResponse)

GetOtherInfoRequest = _reflection.GeneratedProtocolMessageType('GetOtherInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOTHERINFOREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetOtherInfoRequest)
  })
_sym_db.RegisterMessage(GetOtherInfoRequest)

GetOtherInfoResponse = _reflection.GeneratedProtocolMessageType('GetOtherInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOTHERINFORESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetOtherInfoResponse)
  })
_sym_db.RegisterMessage(GetOtherInfoResponse)

GetAllAddressRequest = _reflection.GeneratedProtocolMessageType('GetAllAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLADDRESSREQUEST,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetAllAddressRequest)
  })
_sym_db.RegisterMessage(GetAllAddressRequest)

GetAllAddressResponse = _reflection.GeneratedProtocolMessageType('GetAllAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLADDRESSRESPONSE,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetAllAddressResponse)
  })
_sym_db.RegisterMessage(GetAllAddressResponse)

GetSettlementMethodRsp = _reflection.GeneratedProtocolMessageType('GetSettlementMethodRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETSETTLEMENTMETHODRSP,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetSettlementMethodRsp)
  })
_sym_db.RegisterMessage(GetSettlementMethodRsp)

GetGiftMoneyRsp = _reflection.GeneratedProtocolMessageType('GetGiftMoneyRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETGIFTMONEYRSP,
  '__module__' : 'agentsrv_pb2'
  # @@protoc_insertion_point(class_scope:agent.srv.GetGiftMoneyRsp)
  })
_sym_db.RegisterMessage(GetGiftMoneyRsp)


DESCRIPTOR._options = None

_AGENTMANAGER = _descriptor.ServiceDescriptor(
  name='AgentManager',
  full_name='agent.srv.AgentManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=813,
  serialized_end=1484,
  methods=[
  _descriptor.MethodDescriptor(
    name='VerifyAgent',
    full_name='agent.srv.AgentManager.VerifyAgent',
    index=0,
    containing_service=None,
    input_type=_VERIFYAGENTREQUEST,
    output_type=_VERIFYAGENTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyToken',
    full_name='agent.srv.AgentManager.VerifyToken',
    index=1,
    containing_service=None,
    input_type=_VERIFYTOKENREQUEST,
    output_type=_VERIFYTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpperScoreURL',
    full_name='agent.srv.AgentManager.UpperScoreURL',
    index=2,
    containing_service=None,
    input_type=_UPPERSCOREURLREQUEST,
    output_type=_UPPERSCOREURLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAgent',
    full_name='agent.srv.AgentManager.UpdateAgent',
    index=3,
    containing_service=None,
    input_type=_UPDATEAGENTREQUEST,
    output_type=_UPDATEAGENTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOtherInfo',
    full_name='agent.srv.AgentManager.GetOtherInfo',
    index=4,
    containing_service=None,
    input_type=_GETOTHERINFOREQUEST,
    output_type=_GETOTHERINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllAddress',
    full_name='agent.srv.AgentManager.GetAllAddress',
    index=5,
    containing_service=None,
    input_type=_GETALLADDRESSREQUEST,
    output_type=_GETALLADDRESSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSettlementMethod',
    full_name='agent.srv.AgentManager.GetSettlementMethod',
    index=6,
    containing_service=None,
    input_type=_GETOTHERINFOREQUEST,
    output_type=_GETSETTLEMENTMETHODRSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGiftMoney',
    full_name='agent.srv.AgentManager.GetGiftMoney',
    index=7,
    containing_service=None,
    input_type=_GETOTHERINFOREQUEST,
    output_type=_GETGIFTMONEYRSP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENTMANAGER)

DESCRIPTOR.services_by_name['AgentManager'] = _AGENTMANAGER

# @@protoc_insertion_point(module_scope)