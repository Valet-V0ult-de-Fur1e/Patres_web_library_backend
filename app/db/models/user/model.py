from app.db.base_table_model import BaseModel
from app.db.annotations import *
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserModel(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    books = relationship("BookModel", secondary="book_user_associations", back_populates='users')
    extend_existing = True
