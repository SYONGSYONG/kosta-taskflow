from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    start_date: date
    end_date: date


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    created_at: datetime

    model_config = {"from_attributes": True}
