# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/audio_streaming.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bproto/audio_streaming.proto\x12\x05proto\"F\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x05\x12\x15\n\rsend_finished\x18\x03 \x01(\x08\"5\n\x11RecognitionResult\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x10\n\x08\x66inished\x18\x02 \x01(\x08\x32T\n\x12\x41udioStreamService\x12>\n\x0bStreamAudio\x12\x11.proto.AudioChunk\x1a\x18.proto.RecognitionResult(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.audio_streaming_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUDIOCHUNK']._serialized_start=38
  _globals['_AUDIOCHUNK']._serialized_end=108
  _globals['_RECOGNITIONRESULT']._serialized_start=110
  _globals['_RECOGNITIONRESULT']._serialized_end=163
  _globals['_AUDIOSTREAMSERVICE']._serialized_start=165
  _globals['_AUDIOSTREAMSERVICE']._serialized_end=249
# @@protoc_insertion_point(module_scope)
