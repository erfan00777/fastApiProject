from pydantic import BaseModel
from datetime import datetime


class RequestSchema(BaseModel):
    user_id: int
    created_at: datetime
    page_url: str

class ResponseSchema(BaseModel):
    url: str
    count: int