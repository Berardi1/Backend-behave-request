# Backend Behave Requests

API test automation project built with **Python**, **Behave** and **Requests**, using [JSONPlaceholder](https://jsonplaceholder.typicode.com/) as the API under test.

The project covers basic REST API operations through BDD scenarios, including:

* GET
* POST
* PUT
* DELETE
* HTTP status code validation
* JSON response field validation

## Tech Stack

* Python
* Behave
* Requests
* JSONPlaceholder REST API

## Project Structure

```text
Backend-behave-request/
├── features/
│   ├── create_post.feature
│   ├── delete_post.feature
│   ├── get_post.feature
│   └── update_post.feature
├── steps/
│   └── implementation.py
├── support/
│   └── api_request.py
├── behave.ini
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

* Python 3
* pip

### 1. Clone the repository

```bash
git clone https://github.com/Berardi1/Backend-behave-request.git
cd Backend-behave-request
```

### 2. Create a virtual environment

**Windows:**

```powershell
py -m venv venv
```

Activate it with:

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Test Execution

Run the complete test suite with:

```bash
behave
```

The current suite contains scenarios covering the main CRUD operations against JSONPlaceholder.

## Test Coverage

| Feature     | HTTP Method | Validation                    |
| ----------- | ----------- | ----------------------------- |
| Create post | POST        | Status code and response body |
| Get post    | GET         | Response body                 |
| Update post | PUT         | Status code and response body |
| Delete post | DELETE      | Status code                   |

## API Under Test

The project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free fake REST API commonly used for testing and prototyping.

Base URL:

```text
https://jsonplaceholder.typicode.com/
```

## Notes

This project is intended as a practical example of API test automation using **BDD**, with reusable request handling and response validation separated from the feature specifications.
