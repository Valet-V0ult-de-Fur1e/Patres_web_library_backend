from typing import Annotated, List
from datetime import datetime
from sqlalchemy import ARRAY, String, func
from sqlalchemy.orm import mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True)]
create_time = Annotated[datetime, mapped_column(server_default=func.now())]
update_time = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]
array_or_none_an = Annotated[List[str] | None, mapped_column(ARRAY(String))]