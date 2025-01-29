from datetime import datetime
from pydantic import BaseModel, Field, model_validator

class SBookUserAssociationAdd(BaseModel):
    book_id: int
    user_id: int
    rent_start_date: datetime = Field(datetime_format="%Y-%m-%d")
    rent_end_date: datetime = Field(datetime_format="%Y-%m-%d")
        
        
    @model_validator(mode='before')
    def validate_atts(cls, values):
        rent_start_date_v = values.get('rent_start_date')
        rent_end_date_v = values.get('rent_end_date')
        if rent_end_date_v < rent_start_date_v:
            raise ValueError('Некорректное время возрата')
        return values