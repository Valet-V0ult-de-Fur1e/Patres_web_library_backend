from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class SBookAdd(BaseModel):
    title: str
    publication_date: datetime = Field(datetime_format="%Y-%m-%d")
    count_copies: int
    
    @field_validator('publication_date')
    def check_age(cls, value): 
        if value.timestamp() > datetime.now().timestamp():
            raise ValueError('Ошибка даты')
        return value