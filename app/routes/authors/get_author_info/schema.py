from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from app.routes.books.get_book_info.schema import BookBase


class AuthorBase(BaseModel):
    author_id: int
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия, от 1 до 50 символов")
    biography: str = Field(..., min_length=0, max_length=2500, description="Биография, до 50 символов")
    birth_date: datetime = Field(datetime_format="%Y/%m/%d")

    class Config:
        orm_mode = True


class SAuthorGet(AuthorBase):
    books: List[BookBase]