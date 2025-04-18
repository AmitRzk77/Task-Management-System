 Task Management System - Django REST Framework

A simple Task Management System built using **Django** and **Django REST Framework (DRF)**. This project supports user registration, login with token authentication, role-based permissions (admin and user), and task assignment and tracking.

---

 Features

- User Registration and Login (Token-based Authentication)
- Role-based access: Admins & Regular Users
- Admins can:
  - Create, update, delete any task
  - Assign tasks to users
- Users can:
  - View tasks assigned to them
  - Update task status (if allowed)
- Task filtering by status and due date
- API accessible via browser (with token) or Postman

---

 Tech Stack

- Python 3.13+
- Django 5.2
- Django REST Framework
- SQLite (default) for database

---

 Setup Instructions

1. Clone the repository

```bash
https://github.com/your-username/task-management-system.git
cd task-management-system
```

2. Create and activate virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py migrate
```

5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to access the admin panel.

---

Authentication

Token-based login:
- Register via `POST /api/users/register/`
- Login via `POST /api/users/login/` with username and password
- Receive a token, and send it in the `Authorization` header like:

```http
Authorization: Token <your_token_here>
```

---

API Endpoints Overview

User Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/users/register/ | POST | Register a new user |
| /api/users/login/ | POST | Login and receive a token |
| /api/users/profile/ | GET | View current user info |

Task Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/tasks/ | GET/POST | List tasks / Create task (admin only) |
| /api/tasks/{id}/ | GET/PUT/DELETE | Task detail, update or delete |
| /api/tasks/{id}/status/ | PATCH | Update status (assigned user or admin) |

Filtering Tasks:
- `/api/tasks/?status=pending`
- `/api/tasks/?due_date=2025-04-20`

---

Roles & Permissions

| Role | Permissions |
|------|-------------|
| Admin | Create/assign/edit/delete any task |
| User | View/update own tasks |

---
Swagger/OpenAPI documentation

To-Do (Improvements)

- Password reset support
- Pagination for task list
- Email notifications

---

License

This project is licensed under the MIT License.

---

Acknowledgements

- Django REST Framework
- Python Software Foundation

---

Happy coding! 

