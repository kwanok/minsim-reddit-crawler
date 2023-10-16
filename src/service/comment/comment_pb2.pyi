from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NewCommentRequest(_message.Message):
    __slots__ = ["id", "author", "body", "body_html", "created_utc", "distinguished", "edited", "is_submitter", "link_id", "parent_id", "permalink", "stickied", "submission", "subreddit", "subreddit_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BODY_HTML_FIELD_NUMBER: _ClassVar[int]
    CREATED_UTC_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELD_NUMBER: _ClassVar[int]
    IS_SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMALINK_FIELD_NUMBER: _ClassVar[int]
    STICKIED_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    author: str
    body: str
    body_html: str
    created_utc: int
    distinguished: str
    edited: bool
    is_submitter: bool
    link_id: str
    parent_id: str
    permalink: str
    stickied: bool
    submission: str
    subreddit: str
    subreddit_id: str
    def __init__(self, id: _Optional[str] = ..., author: _Optional[str] = ..., body: _Optional[str] = ..., body_html: _Optional[str] = ..., created_utc: _Optional[int] = ..., distinguished: _Optional[str] = ..., edited: bool = ..., is_submitter: bool = ..., link_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., permalink: _Optional[str] = ..., stickied: bool = ..., submission: _Optional[str] = ..., subreddit: _Optional[str] = ..., subreddit_id: _Optional[str] = ...) -> None: ...

class NewCommentResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
