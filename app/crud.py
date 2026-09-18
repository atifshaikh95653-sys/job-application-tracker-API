from sqlalchemy.orm import Session

from models import JobApplication
from schemas import JobApplicationCreate


def create_application(
    db: Session,
    application: JobApplicationCreate
):
    new_application = JobApplication(
        company=application.company,
        position=application.position,
        location=application.location,
        job_type=application.job_type,
        status=application.status,
        application_date=application.application_date,
        job_url=application.job_url
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application


def get_applications(db: Session):
    return db.query(JobApplication).all()


def get_application(
    db: Session,
    application_id: int
):
    return db.query(JobApplication).filter(
        JobApplication.id == application_id
    ).first()


def update_application(
    db: Session,
    application_id: int,
    application: JobApplicationCreate
):
    existing = get_application(db, application_id)

    if existing is None:
        return None

    existing.company = application.company
    existing.position = application.position
    existing.location = application.location
    existing.job_type = application.job_type
    existing.status = application.status
    existing.application_date = application.application_date
    existing.job_url = application.job_url

    db.commit()
    db.refresh(existing)

    return existing


def delete_application(
    db: Session,
    application_id: int
):
    application = get_application(db, application_id)

    if application is None:
        return None

    db.delete(application)
    db.commit()

    return application