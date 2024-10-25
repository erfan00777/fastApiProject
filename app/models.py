from pydantic import BaseModel
from datetime import datetime

class TrafficData(BaseModel):
    user_id: int
    created_at: datetime
    page_url: str