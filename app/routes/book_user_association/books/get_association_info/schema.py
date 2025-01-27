from pydantic import BaseModel

class SBookUserAssociationGet(BaseModel):
    book_id: int
    author_id: int
