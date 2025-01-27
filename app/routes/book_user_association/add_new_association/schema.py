from pydantic import BaseModel

class SBookUserAssociationAdd(BaseModel):
    book_id: int
    user_id: int
