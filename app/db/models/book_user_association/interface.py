from app.db.base_table_interface import BaseInterface

from app.db import async_session_maker
from sqlalchemy import delete
from sqlalchemy.future import select

from app.db.models.book_user_association.model import BookUserAssociationModel

class BookUserAssociationInterFace(BaseInterface):
    model = BookUserAssociationModel

    @classmethod
    async def add_new_book_user_association(cls, **association_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_association = cls.model(**association_data)
                session.add(new_association)
                await session.flush()
                await session.commit()
                return True
    
    @classmethod
    async def delete_association_by_id(cls, user_id: int, book_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(user_id=user_id).filter_by(book_id=book_id)
                result = await session.execute(query)
                association_to_delete = result.scalar_one_or_none()
                if not association_to_delete:
                    return None
                await session.execute(
                    delete(cls.model).where(cls.model.user_id==user_id).where(cls.model.book_id==book_id)
                )
                await session.commit()
                return True
    
    @classmethod
    async def delete_association_by_user_id(cls, user_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                await session.execute(
                    delete(cls.model).where(cls.model.user_id==user_id)
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