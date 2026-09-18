from datetime import date

from pydantic import BaseModel


class JobApplicationCreate(BaseModel):
    company: str
    position: str
    location: str | None = None
    job_type: str | None = None
    status: str = "Applied"
    application_date: date | None = None
    job_url: str | None = None


class JobApplicationResponse(JobApplicationCreate):
    id: int

    class Config:
        from_attributes = True