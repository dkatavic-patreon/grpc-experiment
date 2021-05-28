# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sidecar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sidecar.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsidecar.proto\",\n\rMessageConfig\x12\x1b\n\x13in_transit_messages\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"#\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t2\x87\x01\n\x07SideCar\x12(\n\ngetMessage\x12\x0e.MessageConfig\x1a\x08.Message\"\x00\x12\x30\n\x10getMessageStream\x12\x0e.MessageConfig\x1a\x08.Message\"\x00\x30\x01\x12 \n\nackMessage\x12\x08.Message\x1a\x06.Empty\"\x00\x62\x06proto3'
)




_MESSAGECONFIG = _descriptor.Descriptor(
  name='MessageConfig',
  full_name='MessageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='in_transit_messages', full_name='MessageConfig.in_transit_messages', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=17,
  serialized_end=61,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=63,
  serialized_end=70,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Message.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='Message.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['MessageConfig'] = _MESSAGECONFIG
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageConfig = _reflection.GeneratedProtocolMessageType('MessageConfig', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGECONFIG,
  '__module__' : 'sidecar_pb2'
  # @@protoc_insertion_point(class_scope:MessageConfig)
  })
_sym_db.RegisterMessage(MessageConfig)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'sidecar_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'sidecar_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)



_SIDECAR = _descriptor.ServiceDescriptor(
  name='SideCar',
  full_name='SideCar',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=245,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMessage',
    full_name='SideCar.getMessage',
    index=0,
    containing_service=None,
    input_type=_MESSAGECONFIG,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMessageStream',
    full_name='SideCar.getMessageStream',
    index=1,
    containing_service=None,
    input_type=_MESSAGECONFIG,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ackMessage',
    full_name='SideCar.ackMessage',
    index=2,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIDECAR)

DESCRIPTOR.services_by_name['SideCar'] = _SIDECAR

# @@protoc_insertion_point(module_scope)