from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils import get_server_data
from app.routes.auth.router import router as router_auth
from app.routes.authors.router import router as router_authors
from app.routes.books.router import router as router_books
from app.routes.book_author_association.router import router as router_book_author_association
from app.routes.book_user_association.router import router as router_book_user_association
from app.routes.users.router import router as router_users


host, port = get_server_data()
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(router_auth)
app.include_router(router_authors)
app.include_router(router_books)
app.include_router(router_book_author_association)
app.include_router(router_book_user_association)
app.include_router(router_users)