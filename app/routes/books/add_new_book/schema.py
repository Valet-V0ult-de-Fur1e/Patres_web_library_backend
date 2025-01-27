from datetime import datetime
from pydantic import BaseModel, field_validator

class SBookAdd(BaseModel):
    title: str
    publication_date: datetime
    count_copies: int
    
    @field_validator('publication_date')
    def check_age(cls, value): 
        if value < datetime.now():
            raise ValueError('Ошибка даты')
        return value