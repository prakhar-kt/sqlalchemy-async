# SQLAlchemy Async Authentication Backend

A modern, asynchronous authentication backend built with FastAPI and SQLAlchemy, featuring JWT token-based authentication and secure password management.

## Features

- 🚀 **Async/Await Support**: Built with Python's async capabilities for high performance
- 🔐 **JWT Authentication**: Secure token-based authentication system
- 🗄️ **SQLAlchemy ORM**: Modern async SQLAlchemy with SQLite backend
- 🔒 **Password Security**: bcrypt hashing with passlib utilities
- 📧 **Email Validation**: Built-in email validation with Pydantic
- ⚡ **FastAPI Framework**: High-performance web framework with automatic API docs
- 🎯 **User Management**: Complete user registration, authentication, and profile management

## Technology Stack

- **Python**: >=3.11
- **Web Framework**: FastAPI with standard extras
- **Database**: SQLAlchemy (async) with aiosqlite
- **Authentication**: 
  - bcrypt for password hashing
  - passlib for password utilities  
  - python-jose for JWT tokens
- **Validation**: Pydantic with email validation
- **Configuration**: python-decouple for environment management
- **Package Management**: uv for fast dependency resolution

## Project Structure

```
sqlalchemy-async/
├── app/
│   ├── account/           # User account management
│   │   ├── models.py     # Database models (User, RefreshToken)
│   │   ├── schemas.py    # Pydantic models for validation
│   │   ├── routers.py    # FastAPI route handlers
│   │   ├── services.py   # Business logic layer
│   │   ├── utils.py      # Utility functions
│   │   └── dependencies.py # FastAPI dependencies
│   ├── db/
│   │   └── config.py     # Database configuration and setup
│   └── main.py           # FastAPI application setup
├── main.py               # Application entry point
├── pyproject.toml        # Project configuration
└── uv.lock              # Dependency lock file
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- uv package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sqlalchemy-async
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Run the application**
   ```bash
   # Using uv
   uv run python app/main.py
   
   # Or directly
   python app/main.py
   ```

### Development Commands

```bash
# Install dependencies
uv sync

# Add new dependencies
uv add <package-name>

# Add development dependencies
uv add --dev <package-name>

# Run the application
uv run python app/main.py

# Start development server (if uvicorn is added)
uv run uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access:

- **Interactive API docs (Swagger)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Database

The application uses SQLite with async support via aiosqlite. The database file (`sqlite.db`) is created automatically in the project root when you first run the application.

### Models

- **User**: Core user model with email, name, and authentication fields
- **RefreshToken**: JWT refresh token management

## Configuration

The application supports environment-based configuration using python-decouple. Create a `.env` file in the project root for custom settings:

```env
# Database
DATABASE_URL=sqlite+aiosqlite:///./sqlite.db

# JWT Settings
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Authentication Flow

1. **User Registration**: POST to `/register` with user details
2. **Login**: POST to `/login` with email and password
3. **Token Refresh**: Use refresh tokens to get new access tokens
4. **Protected Routes**: Include JWT token in Authorization header

## API Endpoints

### Authentication
- `POST /register` - User registration
- `POST /login` - User login
- `POST /refresh` - Refresh access token
- `POST /logout` - User logout

### User Management  
- `GET /me` - Get current user profile
- `PUT /me` - Update user profile
- `DELETE /me` - Delete user account

## Development Status

This project is in early development. Current implemented features:
- ✅ Database models and configuration
- ✅ User schemas and validation
- ✅ FastAPI application setup
- ✅ Database table creation
- 🚧 Authentication endpoints (in progress)
- 🚧 JWT token management (in progress)
- 🚧 Password reset functionality (in progress)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.
