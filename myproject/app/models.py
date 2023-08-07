from panther.db import Model
from pydantic import BaseModel


class BookSerializer(BaseModel):
    name: str
    author: str
    pages_count: int