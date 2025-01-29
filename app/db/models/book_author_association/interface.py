from app.db.base_table_interface import BaseInterface
from app.db.models.book_author_association.model import BookAuthorAssociationModel
from app.db import async_session_maker
from sqlalchemy import delete
from sqlalchemy.future import select

class BookAuthorAssociationInterFace(BaseInterface):
    model = BookAuthorAssociationModel

    @classmethod
    async def add_new_book_author_association(cls, **association_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_association = cls.model(**association_data)
                session.add(new_association)
                await session.flush()
                await session.commit()
                return True
    
    @classmethod
    async def delete_association_by_id(cls, author_id: int, book_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(author_id=author_id).filter_by(book_id=book_id)
                result = await session.execute(query)
                association_to_delete = result.scalar_one_or_none()
                if not association_to_delete:
                    return None
                await session.execute(
                    delete(cls.model).where(cls.model.author_id==author_id).where(cls.model.book_id==book_id)
                )
                await session.commit()
                return True
    
    @classmethod
    async def delete_association_by_author_id(cls, author_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                await session.execute(
                    delete(cls.model).where(cls.model.author_id==author_id)
                )
                await session.commit()
                return True
    
    @classmethod
    async def delete_association_by_book_id(cls, book_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                await session.execute(
                    delete(cls.model).where(cls.model.book_id==book_id)
                )
                await session.commit()
                return True