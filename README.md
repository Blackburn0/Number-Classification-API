# Number Classification API

## Overview
The **Number Classification API** is a RESTful service that classifies a given number based on its mathematical properties. It returns information such as whether the number is prime, perfect, or an Armstrong number, along with its digit sum and a fun fact retrieved from the Numbers API.

## Features
- Accepts a number as a query parameter.
- Determines if the number is:
  - Prime
  - Perfect
  - Armstrong
  - Odd or Even
- Computes the sum of the digits of the number.
- Fetches a fun fact about the number from the Numbers API.
- Returns responses in JSON format.
- Handles invalid inputs gracefully with proper error responses.
- Deployed on a publicly accessible endpoint.
- Implements CORS handling.

## Technology Stack
- **Backend**: Fast API (Python)
- **External API**: Numbers API (http://numbersapi.com/)
- **Deployment**: vercel
- **Version Control**: Git & GitHub

## API Specification
### Endpoint:
```
GET https://number-classification-api-kappa.vercel.app/api/classify-number?number=371
```

### Request Parameters:
- **number** (required): An integer value to classify.

### Response Format:
#### Success Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
#### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/Blackburn0/Number-Classification-API.git
cd number-classification-api
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
