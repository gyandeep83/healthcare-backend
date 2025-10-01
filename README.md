🏥 Healthcare Backend API

A backend system for a healthcare application built with Django, Django REST Framework (DRF), and PostgreSQL.
It provides secure user authentication with JWT and APIs for managing patients, doctors, and patient-doctor mappings.

🚀 Features

✅ User Authentication (Register/Login with JWT)
✅ Patient Management (CRUD APIs)
✅ Doctor Management (CRUD APIs)
✅ Patient–Doctor Mapping (Assign/remove doctors to patients)
✅ Secure Access (APIs restricted to authenticated users)

⚙️ Tech Stack

Python 3.10+
Django 5+
Django REST Framework
PostgreSQL
djangorestframework-simplejwt (JWT authentication)

📦 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/<your-username>/healthcare-backend.git
cd healthcare-backend

2️⃣ Create & Activate Virtual Environment

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Configure Database
Ensure PostgreSQL is running.
Create a database:
CREATE DATABASE healthcare_db;

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Run Server
python manage.py runserver


🔑 Authentication (JWT)
Register: POST /api/register/
Login: POST /api/token/ → Returns access and refresh tokens.
Use JWT in headers:
Authorization: Bearer <access_token>


📖 API Endpoints
👤 Users
POST /api/register/ → Register new user
POST /api/token/ → Login & get JWT token

🧑‍⚕️ Doctors

POST /api/doctors/ → Add a doctor
GET /api/doctors/ → List all doctors
GET /api/doctors/<id>/ → Get doctor details
PUT /api/doctors/<id>/ → Update doctor
DELETE /api/doctors/<id>/ → Delete doctor

🧑‍🤝‍🧑 Patients

POST /api/patients/ → Add patient
GET /api/patients/ → List all patients
GET /api/patients/<id>/ → Get patient details
PUT /api/patients/<id>/ → Update patient
DELETE /api/patients/<id>/ → Delete patient

🔗 Mappings
POST /api/mappings/ → Assign doctor to patient
GET /api/mappings/ → List all mappings
GET /api/mappings/<patient_id>/ → Get doctors for a patient
DELETE /api/mappings/<id>/ → Remove mapping

👨‍💻 Author
Gyandeep – Backend Developer Intern Assignment


