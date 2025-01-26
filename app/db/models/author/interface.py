from app.db.base_table_interface import BaseInterface
from app.db.models.author.model import AuthorModel
from app.db import async_session_maker
from sqlalchemy import delete
from sqlalchemy.future import select

class AuthorInterFace(BaseInterface):
    model = AuthorModel
    
    @classmethod
    async def add_new_author(cls, **author_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_author = cls.model(**author_data)
                session.add(new_author)
                await session.flush()
                new_author_id = new_author.id
                await session.commit()
                return new_author_id
    
    @classmethod
    async def delete_author_by_id(cls, author_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=author_id)
                result = await session.execute(query)
                author_to_delete = result.scalar_one_or_none()
                if not author_to_delete:
                    return None
                await session.execute(
                    delete(cls.model).filter_by(id=author_id)
                )
                await session.commit()
                return author_id

    