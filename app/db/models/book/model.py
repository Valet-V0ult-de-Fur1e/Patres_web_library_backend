from datetime import datetime
from typing import List
from app.db.base_table_model import BaseModel
from app.db.annotations import *
from sqlalchemy.orm import Mapped, relationship


class BookModel(BaseModel):
    __tablename__ = 'books'
    id: Mapped[int_pk]
    title: Mapped[str]
    publication_date: Mapped[datetime]
    count_copies: Mapped[int] = mapped_column(default=0)
    authors = relationship("AuthorModel", secondary="book_author_association", back_populates='books')
    extend_existing = True
