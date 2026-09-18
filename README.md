# 💼 Job Application Tracker API

> A production-style REST API for managing and tracking job & internship applications.

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)](https://www.sqlalchemy.org/)
[![API](https://img.shields.io/badge/API-REST-orange)]()

---

## 📌 About The Project

**Job Application Tracker API** is a backend REST API developed using **FastAPI, PostgreSQL and SQLAlchemy**.

It allows users to manage their job and internship applications through APIs. The project demonstrates practical backend development concepts including **RESTful API design, database integration, CRUD operations, request validation and automatic API documentation**.

This project is built as a portfolio project to demonstrate real-world **Python backend development** skills.

---

## ✨ Key Features

* ✅ Create job/internship applications
* 📋 View all applications
* 🔍 View an application by ID
* ✏️ Update application details
* 🗑️ Delete applications
* 🗄️ PostgreSQL database integration
* 🔗 SQLAlchemy ORM
* 🛡️ Pydantic request validation
* 📚 Interactive Swagger API documentation
* ⚡ Fast and lightweight FastAPI backend
* 🔐 Environment variables for database configuration

---

## 🏗️ Project Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── API Routes
   │
   ├── Pydantic Schemas
   │
   ├── CRUD Operations
   │
   └── SQLAlchemy ORM
          │
          ▼
     PostgreSQL
```

---

## 🛠️ Tech Stack

| Technology       | Purpose                    |
| ---------------- | -------------------------- |
| 🐍 Python        | Backend programming        |
| ⚡ FastAPI        | REST API framework         |
| 🐘 PostgreSQL    | Relational database        |
| 🔗 SQLAlchemy    | ORM / database interaction |
| 🛡️ Pydantic     | Data validation            |
| 🔌 psycopg2      | PostgreSQL driver          |
| 🔐 python-dotenv | Environment configuration  |
| 🚀 Uvicorn       | ASGI server                |

---

## 📂 Project Structure

```text
job-application-tracker-api/
│
├── app/
│   ├── main.py          # API routes
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── crud.py          # Database CRUD operations
│
├── .gitignore
├── .env                 # Local environment variables
└── README.md
```

---

## 🔗 API Endpoints

|  Method  | Endpoint             | Description           |
| :------: | -------------------- | --------------------- |
|   `GET`  | `/`                  | Check API status      |
|  `POST`  | `/applications`      | Create application    |
|   `GET`  | `/applications`      | Get all applications  |
|   `GET`  | `/applications/{id}` | Get application by ID |
|   `PUT`  | `/applications/{id}` | Update application    |
| `DELETE` | `/applications/{id}` | Delete application    |

---

## 📥 Example Request

### Create Application

**POST**

```http
/applications
```

### JSON Body

```json
{
  "company": "Google",
  "position": "Python Developer Intern",
  "location": "Mumbai",
  "job_type": "Internship",
  "status": "Applied",
  "application_date": "2026-09-18",
  "job_url": "https://example.com/job"
}
```

### Response

```json
{
  "id": 1,
  "company": "Google",
  "position": "Python Developer Intern",
  "location": "Mumbai",
  "job_type": "Internship",
  "status": "Applied",
  "application_date": "2026-09-18",
  "job_url": "https://example.com/job"
}
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/atifshaikh95653-sys/job-application-tracker-API.git
```

### 2. Navigate to the Project

```bash
cd job-application-tracker-API
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### 6. Configure PostgreSQL

Create a PostgreSQL database and configure the connection inside `.env`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/job_tracker
```

> ⚠️ Never upload your `.env` file or database credentials to GitHub.

---

## ▶️ Run the API

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can test all API endpoints directly from Swagger UI without using a separate API client.

---

## 🧠 Backend Concepts Demonstrated

This project demonstrates practical knowledge of:

* REST API development
* HTTP methods
* CRUD operations
* Request & response validation
* Path parameters
* Dependency Injection
* Database sessions
* SQLAlchemy ORM
* PostgreSQL integration
* Environment variables
* API documentation
* Backend project structure

---

## 🔮 Future Enhancements

Planned improvements for future versions:

* 🔐 JWT Authentication & Authorization
* 👤 User registration and login
* 🔎 Search and filtering
* 📄 Pagination
* 📊 Application statistics dashboard
* 🏷️ Advanced application status management
* 🗃️ Alembic database migrations
* 📝 Separate update schemas
* ☁️ Cloud deployment
* 🧪 Automated API testing

---

## 🎯 Project Goal

The goal of this project is to build a practical backend system while applying modern Python backend technologies and software development practices.

It is designed as a portfolio project for demonstrating skills in **Python, FastAPI, PostgreSQL, SQLAlchemy and REST API development**.

---

## 👨‍💻 Author

### Atif Shaikh

**Aspiring Python Developer | Backend Developer | B.Sc. IT Student**

🔗 **GitHub:**
https://github.com/atifshaikh95653-sys

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
