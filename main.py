from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Define the data structure for the request body
# This ensures the input is validated and clearly defined.
class NumberList(BaseModel):
    # The 'numbers' key in the request body must contain a list of integers.
    numbers: List[int]

# 3. Define the API endpoint
# This uses a POST request, which is standard for sending data to be processed.
@app.post("/sum_list/")
def sum_of_list(data: NumberList):
    """
    Calculates the sum of the list of numbers provided in the request body.
    """
    # Use the built-in Python sum() function to calculate the total
    total_sum = sum(data.numbers)
    
    # Return the result as a JSON object
    return {
        "input_list": data.numbers,
        "total_sum": total_sum
    }

# Optional: Add a simple GET route for testing the server is running
@app.get("/")
def read_root():
    return {"message": "API is running. Use the /sum_list/ POST endpoint to sum a list."}