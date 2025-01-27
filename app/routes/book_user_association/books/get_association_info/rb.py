class RBBookUserAssociation:
    def __init__(self, book_id: int | None = None,
                 user_id: int | None = None):
        self.book_id = book_id
        self.user_id = user_id

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "book_id": self.book_id,
            "user_id": self.user_id
        }.items() if value is not None}