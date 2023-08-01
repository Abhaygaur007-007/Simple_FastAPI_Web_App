# Import the necessary modules
from fastapi import FastAPI     # The main FastAPI class
from typing import List     # For declaring the type of the input parameter

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the endpoint '/health'
# The HTTP method is GET

@app.get('/health')
def health_check():

    # This method will be executed when a request comes to the '/health' endpoint
    # It simply returns a string "200 OK"

    return "200 OK"


# Define a route for the endpoint '/maximum'
# The HTTP method is POST
# It expects a JSON payload in the request containing a list of integers

@app.post("/maximum/")
def maximum(numbers: List[int]):
    
    if not numbers:     # checks if numbers evaluates to False, which happens when it is an empty list.

        return {"error": "No numbers provided"}  # returns a JSON response with an error message
    
    

    numbers.sort()        # Sorts the input list in ascending order and 
    return {"result": numbers}    # returns the sorted list

# ----------- GET '/health' -------------

"""
curl -X 'GET' \
  'http://127.0.0.1:8000/health' \
  -H 'accept: application/json'

Response body
        "200 OK"

"""

# ----------- POST '/maximum' -------------

"""
curl -X 'POST' \
  'http://127.0.0.1:8000/maximum/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[ 2,1,4,3 ]' 

	
Response body
{
  "result": [ 1,2,3,4 ]
}

"""