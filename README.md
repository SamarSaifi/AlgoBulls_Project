# Django Todo List Application

A clean, efficient, and well-structured Todo List application built with Django and Django REST Framework.

## 🌟 Features

### Core Features
- RESTful API with CRUD operations
- Task management with status tracking
- Tag support with automatic deduplication
- Due date validation
- Comprehensive test coverage

### Security
- Basic Authentication
- Permission-based access control
- Input validation and sanitization

### Developer Experience
- Clean code architecture
- Modular design
- Comprehensive documentation
- Automated testing and CI/CD

## 📁 Project Structure

```
todo_app/
├── api/
│   ├── mixins/
│   │   ├── filtering.py     # Query filtering logic
│   │   └── validation.py    # Validation mixins
│   ├── serializers.py       # API serializers
│   ├── views.py            # API views
│   └── urls.py             # API routing
├── models/
│   ├── task.py            # Task model
│   └── task_status.py     # Status choices
├── utils/
│   ├── validators.py      # Validation utilities
│   └── tag_helpers.py     # Tag management helpers
└── tests/
    ├── unit/             # Unit tests
    ├── integration/      # Integration tests
    └── e2e/             # End-to-end tests
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Django>=4.2.7
- PostgreSQL

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 🔍 Testing

### Run All Tests
```bash
python manage.py test
```

### Run with Coverage
```bash
coverage run manage.py test
coverage report
coverage html  # Generates HTML report
```

### Run E2E Tests
```bash
python manage.py test todo_app.tests.e2e
```


## 🔄 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/tasks/ | List all tasks |
| POST   | /api/tasks/ | Create a task |
| GET    | /api/tasks/{id}/ | Get task details |
| PUT    | /api/tasks/{id}/ | Update a task |
| DELETE | /api/tasks/{id}/ | Delete a task |

### Filtering Tasks
- By status: `/api/tasks/?status=OPEN`
- By tag: `/api/tasks/?tag=important`

## 🔒 Authentication

The API uses Basic Authentication. Include this header in your requests:
```
Authorization: Basic <base64-encoded-credentials>
```

## 📝 Task Model

| Field | Type | Description |
|-------|------|-------------|
| timestamp | DateTime | Auto-set creation time |
| title | String | Task title (max 100 chars) |
| description | Text | Task details (max 1000 chars) |
| due_date | DateTime | Optional due date |
| tags | Array | Optional list of tags |
| status | String | Task status (OPEN, WORKING, etc.) |

## 🔧 Development

### Code Style
- Follow PEP 8 guidelines
- Use Black for formatting
- Run Flake8 for linting

### Running Linters
```bash
black .
flake8
```

### Pre-commit Checks
```bash
# Run before committing
black .
flake8
python manage.py test
```

## 🚀 CI/CD

GitHub Actions workflow includes:
- Unit tests
- Integration tests
- E2E tests
- Code coverage check
- Linting (Black & Flake8)
