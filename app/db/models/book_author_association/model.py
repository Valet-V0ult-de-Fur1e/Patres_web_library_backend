from sqlalchemy import Column, ForeignKey
from app.db.base_table_model import BaseModel
from app.db.annotations import *


class BookAuthorModel(BaseModel):
    __tablename__ = 'book_author_association'
    author_id = Column('author_id', ForeignKey('authors.id'), primary_key=True)
    book_id =  Column('book_id', ForeignKey('books.id'), primary_key=True)
    