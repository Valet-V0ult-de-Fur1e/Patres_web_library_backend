from app.db.base_table_interface import BaseInterface
from app.db.models.book.model import BookModel
from app.db import async_session_maker
from sqlalchemy import delete
from sqlalchemy.future import select

class BookInterFace(BaseInterface):
    model = BookModel
    
    @classmethod
    async def add_new_book(cls, **book_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_book = cls.model(**book_data)
                session.add(new_book)
                await session.flush()
                new_book_id = new_book.id
                await session.commit()
                return new_book_id
    
    @classmethod
    async def delete_book_by_id(cls, book_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=book_id)
                result = await session.execute(query)
                book_to_delete = result.scalar_one_or_none()
                if not book_to_delete:
                    return None
                await session.execute(
                    delete(cls.model).filter_by(id=book_id)
                )
                await session.commit()
                return book_id

    