from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class SAuthorAdd(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия, от 1 до 50 символов")
    biography: str = Field(..., min_length=0, max_length=2500, description="Биография, до 50 символов")
    birth_date: datetime = Field(datetime_format="%Y-%m-%d")
    
    @field_validator('birth_date')
    def check_age(cls, value):
        if value.timestamp() > datetime.now().timestamp():
            raise ValueError('Возраст должен быть больше 18 лет')
        return value