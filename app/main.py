from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db

from schemas import JobApplicationCreate
from schemas import JobApplicationResponse
import crud


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Job Application Tracker API",
    description="Backend API for tracking job and internship applications",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Job Application Tracker API is running"
    }


@app.post(
    "/applications",
    response_model=JobApplicationResponse,
    status_code=201
)
def create_application(
    application: JobApplicationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_application(
        db,
        application
    )


@app.get(
    "/applications",
    response_model=list[JobApplicationResponse]
)
def get_applications(
    db: Session = Depends(get_db)
):
    return crud.get_applications(db)


@app.get(
    "/applications/{application_id}",
    response_model=JobApplicationResponse
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = crud.get_application(
        db,
        application_id
    )

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


@app.put(
    "/applications/{application_id}",
    response_model=JobApplicationResponse
)
def update_application(
    application_id: int,
    application: JobApplicationCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_application(
        db,
        application_id,
        application
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return updated


@app.delete(
    "/applications/{application_id}"
)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = crud.delete_application(
        db,
        application_id
    )

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return {
        "message": "Application deleted successfully"
    }