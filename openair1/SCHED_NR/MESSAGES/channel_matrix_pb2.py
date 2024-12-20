# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: channel_matrix.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='channel_matrix.proto',
  package='NRMatrix',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x63hannel_matrix.proto\x12\x08NRMatrix\"4\n\x0bUE_SRS_PACK\x12%\n\x06UE_SRS\x18\x01 \x03(\x0b\x32\x15.NRMatrix.NR_SRS_PACK\"C\n\x0bNR_SRS_PACK\x12\r\n\x05ue_id\x18\x01 \x02(\x05\x12%\n\x06Matrix\x18\x02 \x03(\x0b\x32\x15.NRMatrix.NR_SRS_INFO\"1\n\x0bNR_SRS_INFO\x12\"\n\x08PRB_ITEM\x18\x01 \x03(\x0b\x32\x10.NRMatrix.RESULT\"%\n\x06RESULT\x12\r\n\x05image\x18\x01 \x02(\x05\x12\x0c\n\x04real\x18\x02 \x02(\x05')
)




_UE_SRS_PACK = _descriptor.Descriptor(
  name='UE_SRS_PACK',
  full_name='NRMatrix.UE_SRS_PACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UE_SRS', full_name='NRMatrix.UE_SRS_PACK.UE_SRS', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=86,
)


_NR_SRS_PACK = _descriptor.Descriptor(
  name='NR_SRS_PACK',
  full_name='NRMatrix.NR_SRS_PACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ue_id', full_name='NRMatrix.NR_SRS_PACK.ue_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Matrix', full_name='NRMatrix.NR_SRS_PACK.Matrix', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=155,
)


_NR_SRS_INFO = _descriptor.Descriptor(
  name='NR_SRS_INFO',
  full_name='NRMatrix.NR_SRS_INFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PRB_ITEM', full_name='NRMatrix.NR_SRS_INFO.PRB_ITEM', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=206,
)


_RESULT = _descriptor.Descriptor(
  name='RESULT',
  full_name='NRMatrix.RESULT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='NRMatrix.RESULT.image', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real', full_name='NRMatrix.RESULT.real', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=245,
)

_UE_SRS_PACK.fields_by_name['UE_SRS'].message_type = _NR_SRS_PACK
_NR_SRS_PACK.fields_by_name['Matrix'].message_type = _NR_SRS_INFO
_NR_SRS_INFO.fields_by_name['PRB_ITEM'].message_type = _RESULT
DESCRIPTOR.message_types_by_name['UE_SRS_PACK'] = _UE_SRS_PACK
DESCRIPTOR.message_types_by_name['NR_SRS_PACK'] = _NR_SRS_PACK
DESCRIPTOR.message_types_by_name['NR_SRS_INFO'] = _NR_SRS_INFO
DESCRIPTOR.message_types_by_name['RESULT'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UE_SRS_PACK = _reflection.GeneratedProtocolMessageType('UE_SRS_PACK', (_message.Message,), dict(
  DESCRIPTOR = _UE_SRS_PACK,
  __module__ = 'channel_matrix_pb2'
  # @@protoc_insertion_point(class_scope:NRMatrix.UE_SRS_PACK)
  ))
_sym_db.RegisterMessage(UE_SRS_PACK)

NR_SRS_PACK = _reflection.GeneratedProtocolMessageType('NR_SRS_PACK', (_message.Message,), dict(
  DESCRIPTOR = _NR_SRS_PACK,
  __module__ = 'channel_matrix_pb2'
  # @@protoc_insertion_point(class_scope:NRMatrix.NR_SRS_PACK)
  ))
_sym_db.RegisterMessage(NR_SRS_PACK)

NR_SRS_INFO = _reflection.GeneratedProtocolMessageType('NR_SRS_INFO', (_message.Message,), dict(
  DESCRIPTOR = _NR_SRS_INFO,
  __module__ = 'channel_matrix_pb2'
  # @@protoc_insertion_point(class_scope:NRMatrix.NR_SRS_INFO)
  ))
_sym_db.RegisterMessage(NR_SRS_INFO)

RESULT = _reflection.GeneratedProtocolMessageType('RESULT', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'channel_matrix_pb2'
  # @@protoc_insertion_point(class_scope:NRMatrix.RESULT)
  ))
_sym_db.RegisterMessage(RESULT)


# @@protoc_insertion_point(module_scope)
