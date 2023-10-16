from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NewSubmissionRequest(_message.Message):
    __slots__ = ["id", "author", "author_flair_text", "clicked", "created_utc", "is_original_content", "is_self", "link_flair_text", "locked", "name", "num_comments", "over_18", "permalink", "score", "selftext", "subreddit", "subreddit_id", "title", "upvote_ratio", "url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FLAIR_TEXT_FIELD_NUMBER: _ClassVar[int]
    CLICKED_FIELD_NUMBER: _ClassVar[int]
    CREATED_UTC_FIELD_NUMBER: _ClassVar[int]
    IS_ORIGINAL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_FIELD_NUMBER: _ClassVar[int]
    LINK_FLAIR_TEXT_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    OVER_18_FIELD_NUMBER: _ClassVar[int]
    PERMALINK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SELFTEXT_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_RATIO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    author: str
    author_flair_text: str
    clicked: bool
    created_utc: int
    is_original_content: bool
    is_self: bool
    link_flair_text: str
    locked: bool
    name: str
    num_comments: int
    over_18: bool
    permalink: str
    score: int
    selftext: str
    subreddit: str
    subreddit_id: str
    title: str
    upvote_ratio: float
    url: str
    def __init__(self, id: _Optional[str] = ..., author: _Optional[str] = ..., author_flair_text: _Optional[str] = ..., clicked: bool = ..., created_utc: _Optional[int] = ..., is_original_content: bool = ..., is_self: bool = ..., link_flair_text: _Optional[str] = ..., locked: bool = ..., name: _Optional[str] = ..., num_comments: _Optional[int] = ..., over_18: bool = ..., permalink: _Optional[str] = ..., score: _Optional[int] = ..., selftext: _Optional[str] = ..., subreddit: _Optional[str] = ..., subreddit_id: _Optional[str] = ..., title: _Optional[str] = ..., upvote_ratio: _Optional[float] = ..., url: _Optional[str] = ...) -> None: ...

class NewSubmissionResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
