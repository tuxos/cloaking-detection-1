# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloaking_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cloaking_detection.proto',
  package='cloaking_detection',
  serialized_pb=_b('\n\x18\x63loaking_detection.proto\x12\x12\x63loaking_detection\"Q\n\x0cLearnedSites\x12.\n\x04site\x18\x01 \x03(\x0b\x32 .cloaking_detection.SitePatterns\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"J\n\x0cSitePatterns\x12\x0c\n\x04name\x18\x01 \x02(\t\x12,\n\x07pattern\x18\x02 \x03(\x0b\x32\x1b.cloaking_detection.Pattern\"L\n\x07Pattern\x12\x0c\n\x04mean\x18\x01 \x02(\x01\x12\x0b\n\x03std\x18\x02 \x02(\x01\x12&\n\x04item\x18\x03 \x03(\x0b\x32\x18.cloaking_detection.Item\")\n\x04Item\x12\x0f\n\x07simhash\x18\x01 \x02(\x04\x12\x10\n\x05\x63ount\x18\x02 \x01(\x04:\x01\x31\"\x92\x01\n\x08HtmlText\x12)\n\x04word\x18\x01 \x03(\x0b\x32\x1b.cloaking_detection.Feature\x12,\n\x07\x62i_gram\x18\x02 \x03(\x0b\x32\x1b.cloaking_detection.Feature\x12-\n\x08tri_gram\x18\x03 \x03(\x0b\x32\x1b.cloaking_detection.Feature\"\x91\x01\n\x07HtmlDom\x12)\n\x04node\x18\x01 \x03(\x0b\x32\x1b.cloaking_detection.Feature\x12,\n\x07\x62i_node\x18\x02 \x03(\x0b\x32\x1b.cloaking_detection.Feature\x12-\n\x08tri_node\x18\x03 \x03(\x0b\x32\x1b.cloaking_detection.Feature\"V\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x11\n\tint_value\x18\x02 \x01(\x05\x12\x14\n\x0c\x64ouble_value\x18\x03 \x01(\x01\x12\x14\n\x0cstring_value\x18\x04 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LEARNEDSITES = _descriptor.Descriptor(
  name='LearnedSites',
  full_name='cloaking_detection.LearnedSites',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='site', full_name='cloaking_detection.LearnedSites.site', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cloaking_detection.LearnedSites.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=129,
)


_SITEPATTERNS = _descriptor.Descriptor(
  name='SitePatterns',
  full_name='cloaking_detection.SitePatterns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cloaking_detection.SitePatterns.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='cloaking_detection.SitePatterns.pattern', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=205,
)


_PATTERN = _descriptor.Descriptor(
  name='Pattern',
  full_name='cloaking_detection.Pattern',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='cloaking_detection.Pattern.mean', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='std', full_name='cloaking_detection.Pattern.std', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='cloaking_detection.Pattern.item', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=283,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='cloaking_detection.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simhash', full_name='cloaking_detection.Item.simhash', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='cloaking_detection.Item.count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=326,
)


_HTMLTEXT = _descriptor.Descriptor(
  name='HtmlText',
  full_name='cloaking_detection.HtmlText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='cloaking_detection.HtmlText.word', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bi_gram', full_name='cloaking_detection.HtmlText.bi_gram', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tri_gram', full_name='cloaking_detection.HtmlText.tri_gram', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=475,
)


_HTMLDOM = _descriptor.Descriptor(
  name='HtmlDom',
  full_name='cloaking_detection.HtmlDom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='cloaking_detection.HtmlDom.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bi_node', full_name='cloaking_detection.HtmlDom.bi_node', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tri_node', full_name='cloaking_detection.HtmlDom.tri_node', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=623,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='cloaking_detection.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cloaking_detection.Feature.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='cloaking_detection.Feature.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='cloaking_detection.Feature.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='cloaking_detection.Feature.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=625,
  serialized_end=711,
)

_LEARNEDSITES.fields_by_name['site'].message_type = _SITEPATTERNS
_SITEPATTERNS.fields_by_name['pattern'].message_type = _PATTERN
_PATTERN.fields_by_name['item'].message_type = _ITEM
_HTMLTEXT.fields_by_name['word'].message_type = _FEATURE
_HTMLTEXT.fields_by_name['bi_gram'].message_type = _FEATURE
_HTMLTEXT.fields_by_name['tri_gram'].message_type = _FEATURE
_HTMLDOM.fields_by_name['node'].message_type = _FEATURE
_HTMLDOM.fields_by_name['bi_node'].message_type = _FEATURE
_HTMLDOM.fields_by_name['tri_node'].message_type = _FEATURE
DESCRIPTOR.message_types_by_name['LearnedSites'] = _LEARNEDSITES
DESCRIPTOR.message_types_by_name['SitePatterns'] = _SITEPATTERNS
DESCRIPTOR.message_types_by_name['Pattern'] = _PATTERN
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['HtmlText'] = _HTMLTEXT
DESCRIPTOR.message_types_by_name['HtmlDom'] = _HTMLDOM
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE

LearnedSites = _reflection.GeneratedProtocolMessageType('LearnedSites', (_message.Message,), dict(
  DESCRIPTOR = _LEARNEDSITES,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.LearnedSites)
  ))
_sym_db.RegisterMessage(LearnedSites)

SitePatterns = _reflection.GeneratedProtocolMessageType('SitePatterns', (_message.Message,), dict(
  DESCRIPTOR = _SITEPATTERNS,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.SitePatterns)
  ))
_sym_db.RegisterMessage(SitePatterns)

Pattern = _reflection.GeneratedProtocolMessageType('Pattern', (_message.Message,), dict(
  DESCRIPTOR = _PATTERN,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.Pattern)
  ))
_sym_db.RegisterMessage(Pattern)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.Item)
  ))
_sym_db.RegisterMessage(Item)

HtmlText = _reflection.GeneratedProtocolMessageType('HtmlText', (_message.Message,), dict(
  DESCRIPTOR = _HTMLTEXT,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.HtmlText)
  ))
_sym_db.RegisterMessage(HtmlText)

HtmlDom = _reflection.GeneratedProtocolMessageType('HtmlDom', (_message.Message,), dict(
  DESCRIPTOR = _HTMLDOM,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.HtmlDom)
  ))
_sym_db.RegisterMessage(HtmlDom)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'cloaking_detection_pb2'
  # @@protoc_insertion_point(class_scope:cloaking_detection.Feature)
  ))
_sym_db.RegisterMessage(Feature)


# @@protoc_insertion_point(module_scope)