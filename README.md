# My FastAPI App

This is a simple web application built with FastAPI in Python 3.11.4 It features two endpoints:

- `/health`: a GET endpoint that returns a `200 OK` status message.
- `/maximum`: a POST endpoint that accepts a list of integers and returns them sorted in ascending order.

## Installation and Setup

### Prerequisites

- Python 3.11.4
- pip (Python package installer)

### Steps

1. Clone the repository or download the project to your local machine.

2. Navigate to the project directory.

3. Set up a Python virtual environment:
   ```bash
   python -m venv fastapi-env

### Activate the virtual environment:

1. On Windows:
   ```bash
   fastapi-env\Scripts\activate

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt

## Running the Application

1. Run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload

You can now access the application at http://localhost:8000.

The interactive API documentation is available at http://localhost:8000/docs.

## Screen Shots

 1. Health EndPoint:
![FastApi_EndPoint_health](https://github.com/Abhaygaur007-007/Simple_FastAPI_Web_App/assets/83288780/99896956-bc6a-4d31-9697-67125a68ef49)

2. Maximum EndPoint:

   ![FastApi_EndPoint_maximum](https://github.com/Abhaygaur007-007/Simple_FastAPI_Web_App/assets/83288780/fc03ef79-0432-4a51-961d-1ae27e6bce50)

## Contact

- Author: Abhay Gaur
