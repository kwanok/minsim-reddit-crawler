from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NewCommentRequest(_message.Message):
    __slots__ = ["content", "author", "subreddit", "created_at", "id", "subreddit_id"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    author: str
    subreddit: str
    created_at: int
    id: str
    subreddit_id: str
    def __init__(
        self,
        content: _Optional[str] = ...,
        author: _Optional[str] = ...,
        subreddit: _Optional[str] = ...,
        created_at: _Optional[int] = ...,
        id: _Optional[str] = ...,
        subreddit_id: _Optional[str] = ...,
    ) -> None: ...

class NewCommentResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
