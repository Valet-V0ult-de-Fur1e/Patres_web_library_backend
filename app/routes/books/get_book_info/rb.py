from datetime import datetime


class RBBook:
    def __init__(self, book_id: int | None = None,
                 title: str | None = None,
                 publication_date: datetime | None = None,
                 count_copies: int | None = None):
        self.id = book_id
        self.title = title
        self.publication_date = publication_date
        self.count_copies = count_copies

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "id": self.id,
            "title": self.title,
            "publication_date": self.publication_date,
            "count_copies": self.count_copies,
        }.items() if value is not None}