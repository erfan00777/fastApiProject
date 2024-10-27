from fastapi import APIRouter, HTTPException
from typing import List
from app.helper import *
from app.models import RequestSchema, ResponseSchema

router = APIRouter()



@router.post("/api/traffic/{request_id}", status_code=201)
async def write_request(request_id: str, request: RequestSchema):
    query = """
    INSERT INTO user_view (request_id, user_id, created_at, page_url)
    VALUES
    """
    # Use formatted values
    values = f"('{request_id}', {request.user_id}, '{request.created_at}', '{request.page_url}')"

    full_query = query + values

    try:
        write_query(full_query)
        return {"message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/traffic/report/{user_id}", response_model=List[ResponseSchema])
async def read_request(user_id: int):
    query = (f"""    
    SELECT page_url, COUNT(*) AS page_view_count 
    FROM user_view Final 
    WHERE user_id =  {user_id}
    AND created_at >= now() - INTERVAL 24 HOUR 
    GROUP BY page_url
    """)
    try:
        results = read_query(query)
        return [{"url": row[0], "count": row[1]} for row in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

