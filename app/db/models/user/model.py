from app.db.base_table_model import BaseModel
from app.db.annotations import *
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.book.model import BookModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    books: Mapped[List['BookModel']] = relationship(secondary="book_user_associations")
    extend_existing = True
