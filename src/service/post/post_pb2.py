# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: post.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\npost.proto\x12\x0bserver.post"\x80\x01\n\x0eNewPostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x11\n\tsubreddit\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x03\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\n\n\x02id\x18\x07 \x01(\t"\x1d\n\x0fNewPostResponse\x12\n\n\x02id\x18\x01 \x01(\t2L\n\x04Post\x12\x44\n\x07NewPost\x12\x1b.server.post.NewPostRequest\x1a\x1c.server.post.NewPostResponseB*Z(github.com/kwanok/minsim-api/server/postb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "post_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z(github.com/kwanok/minsim-api/server/post"
    _globals["_NEWPOSTREQUEST"]._serialized_start = 28
    _globals["_NEWPOSTREQUEST"]._serialized_end = 156
    _globals["_NEWPOSTRESPONSE"]._serialized_start = 158
    _globals["_NEWPOSTRESPONSE"]._serialized_end = 187
    _globals["_POST"]._serialized_start = 189
    _globals["_POST"]._serialized_end = 265
# @@protoc_insertion_point(module_scope)