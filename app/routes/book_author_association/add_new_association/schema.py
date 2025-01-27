from pydantic import BaseModel

class SBookAuthorAssociationAdd(BaseModel):
    book_id: int
    author_id: int
