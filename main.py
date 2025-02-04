from fastapi import FastAPI, Query, HTTPException
import httpx
import math

app = FastAPI()

# CORS setup
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NUMBERS_API_URL = "http://numbersapi.com/{}?json"

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number (using absolute value)."""
    n = abs(n)  # Handle negative numbers
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_perfect(n: int) -> bool:
    """Check if a number is a Perfect number."""
    if n <= 0:
        return False  # Perfect numbers are positive
    return sum(i for i in range(1, n) if n % i == 0) == n

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    """Classifies a number based on mathematical properties, supporting negative numbers."""
    try:
        # Check properties
        armstrong = is_armstrong(number)
        perfect = is_perfect(number)
        is_prime = number > 1 and all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1))
        is_odd = number % 2 != 0

        properties = []
        if armstrong:
            properties.append("armstrong")
        properties.append("odd" if is_odd else "even")

        # Fetch a fun fact
        async with httpx.AsyncClient() as client:
            response = await client.get(NUMBERS_API_URL.format(number))
            fact_data = response.json()
            fun_fact = fact_data.get("text", "No fun fact found.")

        return {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(abs(number))),
            "fun_fact": fun_fact
        }
    
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": "alphabet", "error": True})
