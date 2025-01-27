from pydantic import BaseModel

class SBookAuthorAssociationGet(BaseModel):
    book_id: int
    author_id: int
