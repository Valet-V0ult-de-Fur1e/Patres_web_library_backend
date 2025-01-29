from sqlalchemy import Column, ForeignKey
from app.db.base_table_model import BaseModel
from app.db.annotations import *
from sqlalchemy.orm import Mapped
from datetime import datetime


class BookUserAssociationModel(BaseModel):
    __tablename__ = 'book_user_associations'
    user_id = Column('user_id', ForeignKey('users.id'), primary_key=True)
    book_id =  Column('book_id', ForeignKey('books.id'), primary_key=True)
    rent_start_date: Mapped[datetime]
    rent_end_date: Mapped[datetime]