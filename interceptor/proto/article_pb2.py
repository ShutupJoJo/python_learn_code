# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: article.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rarticle.proto\"J\n\x07\x41rticle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x04 \x01(\t\"5\n\x12\x41rticleListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"1\n\x13\x41rticleListResponse\x12\x1a\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x08.Article\"\"\n\x14\x41rticleDetailRequest\x12\n\n\x02pk\x18\x01 \x01(\x05\"2\n\x15\x41rticleDetailResponse\x12\x19\n\x07\x61rticle\x18\x01 \x01(\x0b\x32\x08.Article2\x8a\x01\n\x0e\x41rticleService\x12\x38\n\x0b\x41rticleList\x12\x13.ArticleListRequest\x1a\x14.ArticleListResponse\x12>\n\rArticleDetail\x12\x15.ArticleDetailRequest\x1a\x16.ArticleDetailResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'article_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ARTICLE']._serialized_start=17
  _globals['_ARTICLE']._serialized_end=91
  _globals['_ARTICLELISTREQUEST']._serialized_start=93
  _globals['_ARTICLELISTREQUEST']._serialized_end=146
  _globals['_ARTICLELISTRESPONSE']._serialized_start=148
  _globals['_ARTICLELISTRESPONSE']._serialized_end=197
  _globals['_ARTICLEDETAILREQUEST']._serialized_start=199
  _globals['_ARTICLEDETAILREQUEST']._serialized_end=233
  _globals['_ARTICLEDETAILRESPONSE']._serialized_start=235
  _globals['_ARTICLEDETAILRESPONSE']._serialized_end=285
  _globals['_ARTICLESERVICE']._serialized_start=288
  _globals['_ARTICLESERVICE']._serialized_end=426
# @@protoc_insertion_point(module_scope)
