# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: glossary.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'glossary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\x08glossary\"8\n\x04Term\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\".\n\x0fGetTermsRequest\x12\x0c\n\x04skip\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"1\n\x10GetTermsResponse\x12\x1d\n\x05terms\x18\x01 \x03(\x0b\x32\x0e.glossary.Term\"!\n\x0eGetTermRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"/\n\x0fGetTermResponse\x12\x1c\n\x04term\x18\x01 \x01(\x0b\x32\x0e.glossary.Term\"9\n\x11\x43reateTermRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"2\n\x12\x43reateTermResponse\x12\x1c\n\x04term\x18\x01 \x01(\x0b\x32\x0e.glossary.Term\"9\n\x11UpdateTermRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"2\n\x12UpdateTermResponse\x12\x1c\n\x04term\x18\x01 \x01(\x0b\x32\x0e.glossary.Term\"$\n\x11\x44\x65leteTermRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"%\n\x12\x44\x65leteTermResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xef\x02\n\x0fGlossaryService\x12\x41\n\x08GetTerms\x12\x19.glossary.GetTermsRequest\x1a\x1a.glossary.GetTermsResponse\x12>\n\x07GetTerm\x12\x18.glossary.GetTermRequest\x1a\x19.glossary.GetTermResponse\x12G\n\nCreateTerm\x12\x1b.glossary.CreateTermRequest\x1a\x1c.glossary.CreateTermResponse\x12G\n\nUpdateTerm\x12\x1b.glossary.UpdateTermRequest\x1a\x1c.glossary.UpdateTermResponse\x12G\n\nDeleteTerm\x12\x1b.glossary.DeleteTermRequest\x1a\x1c.glossary.DeleteTermResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TERM']._serialized_start=28
  _globals['_TERM']._serialized_end=84
  _globals['_GETTERMSREQUEST']._serialized_start=86
  _globals['_GETTERMSREQUEST']._serialized_end=132
  _globals['_GETTERMSRESPONSE']._serialized_start=134
  _globals['_GETTERMSRESPONSE']._serialized_end=183
  _globals['_GETTERMREQUEST']._serialized_start=185
  _globals['_GETTERMREQUEST']._serialized_end=218
  _globals['_GETTERMRESPONSE']._serialized_start=220
  _globals['_GETTERMRESPONSE']._serialized_end=267
  _globals['_CREATETERMREQUEST']._serialized_start=269
  _globals['_CREATETERMREQUEST']._serialized_end=326
  _globals['_CREATETERMRESPONSE']._serialized_start=328
  _globals['_CREATETERMRESPONSE']._serialized_end=378
  _globals['_UPDATETERMREQUEST']._serialized_start=380
  _globals['_UPDATETERMREQUEST']._serialized_end=437
  _globals['_UPDATETERMRESPONSE']._serialized_start=439
  _globals['_UPDATETERMRESPONSE']._serialized_end=489
  _globals['_DELETETERMREQUEST']._serialized_start=491
  _globals['_DELETETERMREQUEST']._serialized_end=527
  _globals['_DELETETERMRESPONSE']._serialized_start=529
  _globals['_DELETETERMRESPONSE']._serialized_end=566
  _globals['_GLOSSARYSERVICE']._serialized_start=569
  _globals['_GLOSSARYSERVICE']._serialized_end=936
# @@protoc_insertion_point(module_scope)