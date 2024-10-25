from pydantic import BaseModel
from datetime import datetime

class check_schema(BaseModel):
    user_id: int
    created_at: datetime
    page_url: str