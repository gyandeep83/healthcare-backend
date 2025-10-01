# 🏥 Healthcare Backend API

A backend system for a healthcare application built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
It provides secure user authentication with **JWT** and APIs for managing patients, doctors, and patient-doctor mappings.

---

## 🚀 Features

- ✅ User Authentication (Register/Login with JWT)  
- ✅ Patient Management (CRUD APIs)  
- ✅ Doctor Management (CRUD APIs)  
- ✅ Patient–Doctor Mapping (Assign/remove doctors to patients)  
- ✅ Secure Access (APIs restricted to authenticated users)  

---

## ⚙️ Tech Stack

- Python 3.10+  
- Django 5+  
- Django REST Framework  
- PostgreSQL  
- djangorestframework-simplejwt (JWT authentication)  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gyandeep83/healthcare-backend.git
cd healthcare-backend
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```
Open .env and fill in your credentials:

Sample .env.example:
```bash
SECRET_KEY='your-django-secret-key'
DEBUG=True
DB_NAME=healthcare_db
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```



### 5️⃣ Configure Database
Make sure PostgreSQL is running and create a database:

```bash
CREATE DATABASE healthcare_db;
```
Update your .env or settings.py with the database credentials.

### 6️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Run Server

```bash
python manage.py runserver
```

### 🔑 Authentication (JWT)
Register: POST /api/register/
Login: POST /api/token/ → Returns access and refresh tokens
Use JWT in headers for authenticated requests:

```bash
Authorization: Bearer <access_token>
```

### 📖 API Endpoints
👤 Users
| Method | Endpoint       | Description           |
| ------ | -------------- | --------------------- |
| POST   | /api/register/ | Register new user     |
| POST   | /api/token/    | Login & get JWT token |

🧑‍⚕️ Doctors
| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| POST   | /api/doctors/      | Add a doctor       |
| GET    | /api/doctors/      | List all doctors   |
| GET    | /api/doctors/<id>/ | Get doctor details |
| PUT    | /api/doctors/<id>/ | Update doctor      |
| DELETE | /api/doctors/<id>/ | Delete doctor      |

🧑‍🤝‍🧑 Patients
| Method | Endpoint            | Description         |
| ------ | --------------------- | ------------------- |
| POST   | /api/patients/      | Add patient         |
| GET    | /api/patients/      | List all patients   |
| GET    | /api/patients/<id>/ | Get patient details |
| PUT    | /api/patients/<id>/ | Update patient      |
| DELETE | /api/patients/<id>/ | Delete patient      |

🔗 Mappings
| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| POST   | /api/mappings/              | Assign doctor to patient  |
| GET    | /api/mappings/              | List all mappings         |
| GET    | /api/mappings/<patient_id>/ | Get doctors for a patient |
| DELETE | /api/mappings/<id>/         | Remove mapping            |

### 👨‍💻 Author
Gyandeep – Backend Developer Intern Assignment



