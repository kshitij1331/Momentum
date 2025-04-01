# Momentum

Momentum is a Django-based project management web application that allows users to create, track, and manage projects and tasks efficiently.

## Features
- User authentication (Login/Signup)
- Project creation, updating, and deletion
- Task management with progress tracking
- Task filtering and sorting
- Dashboard for project overview

## Installation
### Prerequisites
- Python 3.12+
- Django 4.x

### Setup
```sh
# Clone the repository
git clone https://github.com/yourusername/momentum.git
cd momentum

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

## Directory Structure
```
Momentum/
├── dashboard/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_project_owner_remove_task_assigned_to_and_more.py
│   │   ├── 0003_project_owner_task_assigned_to_task_priority_and_more.py
│   │   ├── 0004_remove_project_owner_remove_task_assigned_to_and_more.py
│   │   ├── 0005_project_user.py
│   │   ├── 0006_remove_task_description_task_created_at_and_more.py
│   ├── templates/
│   │   ├── dashboard/
│   │   │   ├── dashboard.html
│   │   │   ├── home.html
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   ├── project_form.html
│   │   │   ├── project_detail.html
│   │   │   ├── project_confirm_delete.html
│   │   │   ├── task_form.html
│   │   │   ├── task_confirm_delete.html
├── momentum/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── static/
│   ├── css/
│   ├── images/
│   ├── js/
├── db.sqlite3
├── manage.py
```

## Usage
- Navigate to `http://127.0.0.1:8000/` in your browser.
- Register an account or log in.
- Create projects and add tasks.
- Track task progress and manage your workflow.
