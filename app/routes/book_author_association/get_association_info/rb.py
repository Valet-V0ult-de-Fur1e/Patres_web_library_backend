class RBBookAuthorAssociation:
    def __init__(self, book_id: int | None = None,
                 author_id: int | None = None):
        self.book_id = book_id
        self.author_id = author_id

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "book_id": self.book_id,
            "author_id": self.author_id
        }.items() if value is not None}