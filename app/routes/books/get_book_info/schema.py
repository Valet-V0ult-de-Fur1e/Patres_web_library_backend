from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, field_validator

from app.routes.authors.get_author_info.schema import AuthorBase

class BookBase(BaseModel):
    book_id: int
    title: str
    publication_date: datetime
    count_copies: int

    class Config:
        orm_mode = True

class SBookGet(BookBase):
    authors: List[AuthorBase]