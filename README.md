# FastAPI Learning Projects

A collection of FastAPI projects I created while learning FastAPI, demonstrating various features and best practices, including a comprehensive Patient Management System and Pydantic validation examples.

## 📁 Project Structure

```
FastAPI/
├── doctor_project/          # Patient Management System
│   ├── main.py             # Main FastAPI application
│   └── patient_data.json   # Patient data storage
├── First_Fastapi/          # Basic FastAPI introduction
│   └── main.py             # Simple Hello World API
└── pydantic/               # Pydantic validation examples
    ├── 1_pydantic_why.py   # Introduction to Pydantic
    ├── 2_field_validator.py # Field validation examples
    ├── 3_model_validator.py # Model validation examples
    ├── 4_computed_fields.py # Computed fields demonstration
    ├── 5_nested_models.py   # Nested model structures
    └── 6_serialization.py   # Data serialization examples
```

## 🚀 Projects Overview

### 1. Patient Management System (`doctor_project/`)

A fully functional REST API for managing patient records with the following features:

#### Features
- **CRUD Operations**: Create, Read, Update, Delete patient records
- **BMI Calculation**: Automatic BMI computation and health verdict
- **Data Validation**: Comprehensive input validation using Pydantic
- **Sorting**: Sort patients by height, weight, or BMI
- **Error Handling**: Proper HTTP status codes and error messages

#### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/about` | API description |
| GET | `/view` | View all patients |
| GET | `/patient/{patient_id}` | Get specific patient |
| GET | `/sort` | Sort patients by field |
| POST | `/create` | Create new patient |
| PUT | `/edit{patient_id}` | Update patient |
| DELETE | `/delete{patient_id}` | Delete patient |

## 📚 API Documentation

Once the server is running, visit:
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc


## 🔧 Key Features Demonstrated

### FastAPI Features
- ✅ Automatic API documentation
- ✅ Type hints and validation
- ✅ Path parameters and query parameters
- ✅ Request/Response models
- ✅ HTTP status codes
- ✅ Error handling
- ✅ JSON serialization

### Pydantic Features
- ✅ Type validation
- ✅ Field constraints
- ✅ Custom validators
- ✅ Computed fields
- ✅ Nested models
- ✅ Data serialization
- ✅ Email validation
- ✅ URL validation

## 🎯 Learning Objectives

This repository contains my learning journey with FastAPI and demonstrates:
- FastAPI framework fundamentals
- RESTful API design principles
- Pydantic data validation
- Type hints and annotations
- Error handling best practices
- API documentation generation
- Data modeling and validation
- Computed fields and business logic

Perfect for developers learning FastAPI, Python web development, and API design patterns!
