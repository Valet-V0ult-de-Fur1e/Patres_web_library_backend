from datetime import datetime
from app.db.base_table_model import BaseModel
from app.db.annotations import *
from sqlalchemy.orm import Mapped, relationship


class AuthorModel(BaseModel):
    __tablename__ = 'authors'
    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    biography: Mapped[str]
    birth_date: Mapped[datetime]
    books = relationship("BookModel", secondary="book_author_associations", back_populates='authors')
    extend_existing = True
