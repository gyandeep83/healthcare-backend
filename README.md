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

### 4️⃣ Configure Database
Make sure PostgreSQL is running and create a database:

```bash
CREATE DATABASE healthcare_db;
```
Update your .env or settings.py with the database credentials.

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run Server

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

📖 API Endpoints
| Method | Endpoint       | Description           |
| ------ | -------------- | --------------------- |
| POST   | /api/register/ | Register new user     |
| POST   | /api/token/    | Login & get JWT token |


