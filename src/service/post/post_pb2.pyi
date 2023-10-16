from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NewPostRequest(_message.Message):
    __slots__ = ["title", "content", "author", "subreddit", "created_at", "url", "id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    author: str
    subreddit: str
    created_at: int
    url: str
    id: str
    def __init__(
        self,
        title: _Optional[str] = ...,
        content: _Optional[str] = ...,
        author: _Optional[str] = ...,
        subreddit: _Optional[str] = ...,
        created_at: _Optional[int] = ...,
        url: _Optional[str] = ...,
        id: _Optional[str] = ...,
    ) -> None: ...

class NewPostResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
