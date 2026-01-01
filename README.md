# FastAPI Course

This is a comprehensive FastAPI course that takes you from the basics to building full-fledged web applications with authentication.

## Prerequisites

- Python 3.12 or higher
- Basic understanding of Python
- Familiarity with HTTP and REST APIs (helpful but not required)

## Course Structure

The course is organized into daily lessons, each building upon the previous one. Each day contains:
- Code examples in `main.py` and other relevant files
- Templates (for days involving HTML rendering)
- A `pyproject.toml` file with dependencies
- A `README.md` with specific topics covered that day

### Day 2: Client-Server Architecture
- Introduction to client-server model
- Basic FastAPI setup

### Day 3: Endpoints
- Creating API endpoints
- Basic routing

### Day 4: Path Parameters, Query Parameters, and POST Requests
- Path parameters with validation
- Query parameters
- POST method with JSON and form data
- Swagger UI introduction

### Day 5: PUT and DELETE Methods
- Updating resources with PUT
- Deleting resources with DELETE
- Enhanced Swagger UI with tags and examples

### Day 6-7: Product API
- Building a complete Product API
- Using slugs
- HTTP exceptions and status codes

### Day 8: Pydantic Features
- Type validation and conversion
- Field validation
- Default values and optional fields
- Nested models and validators
- Model inheritance and aliases

### Day 9: Request/Response Models and Jinja2
- Request and response models
- JSONResponse and HTMLResponse
- Introduction to Jinja2 templating

### Day 10-11: HTML Templates and CRUD Operations
- Building web interfaces with templates
- Complete CRUD operations with HTML forms

### Day 12: PostgreSQL Integration
- Database setup with PostgreSQL
- SQLAlchemy ORM
- Combining FastAPI with databases and templates

### Day 13: Blog Project
- Full blog application
- Jinja2 templates with PostgreSQL

### Day 14: Database Relationships
- Foreign keys
- One-to-many relationships
- Response models
- Error handling with try-except

### Day 15: Modular Code and Environment Variables
- Splitting code into modules
- Environment variables
- JWT overview

### Day 16: Authentication with JWT
- Password hashing
- JSON Web Tokens (JWT)
- User authentication and authorization

## Installation and Setup

Each day is self-contained with its own dependencies. To run a specific day's code:

1. Navigate to the day's directory:
   ```bash
   cd dayX
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt  # if present
   # or
   pip install -e .
   ```

3. Run the application:
   ```bash
   uv run uvicorn main:app --reload
   ```

   Or if using pip:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser to `http://127.0.0.1:8000` to see the API documentation.

## Database Setup (for later days)

For days 12-14, you'll need PostgreSQL:

1. Install PostgreSQL
2. Create a database
3. Update the connection string in the code (usually in `database.py`)

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy Documentation](https://sqlalchemy.org/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## Contributing

Feel free to submit issues or pull requests if you find any errors or have suggestions for improvements.

## License

This course is provided as-is for educational purposes.