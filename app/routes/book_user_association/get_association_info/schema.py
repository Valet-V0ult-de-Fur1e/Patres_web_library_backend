from datetime import datetime
from pydantic import BaseModel, Field

class SBookUserAssociationGet(BaseModel):
    book_id: int
    author_id: int
    rent_start_date: datetime = Field(datetime_format="%Y-%m-%d")
    rent_end_date: datetime = Field(datetime_format="%Y-%m-%d")