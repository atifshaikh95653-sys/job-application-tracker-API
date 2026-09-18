from sqlalchemy import Column, Integer, String, Date

from database import Base


class JobApplication(Base):

    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(100), nullable=False)

    position = Column(String(100), nullable=False)

    location = Column(String(100))

    job_type = Column(String(50))

    status = Column(String(50), default="Applied")

    application_date = Column(Date)

    job_url = Column(String(500))