from app.db.base_table_interface import BaseInterface
from app.db.models.book_author_association.model import BookAuthorModel
from app.db import async_session_maker
from sqlalchemy import delete
from sqlalchemy.future import select

class BookAuthorInterFace(BaseInterface):
    model = BookAuthorModel

    