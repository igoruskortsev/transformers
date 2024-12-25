from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRequest(_message.Message):
    __slots__ = ("text", "themes")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    text: str
    themes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., themes: _Optional[_Iterable[str]] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("themes",)
    THEMES_FIELD_NUMBER: _ClassVar[int]
    themes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, themes: _Optional[_Iterable[str]] = ...) -> None: ...
