from datetime import datetime


class RBAuthor:
    def __init__(self, author_id: int | None = None,
                 first_name: str | None = None,
                 last_name: str | None = None,
                 biography: str | None = None,
                 birth_date: datetime | None = None):
        self.id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography
        self.birth_date = birth_date


    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "biography": self.biography,
            "birth_date": self.birth_date
        }.items() if value is not None}