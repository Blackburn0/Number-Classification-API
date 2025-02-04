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
- **Backend**: Django REST Framework (Python)
- **External API**: Numbers API (http://numbersapi.com/)
- **Database**: SQLite (for local development)
- **Deployment**: vercel
- **Version Control**: Git & GitHub

## API Specification
### Endpoint:
```
GET <your-domain.com>/api/classify-number?number=<number>
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
### Prerequisites
- Python 3.x installed
- Django and required dependencies installed

### Clone the Repository
```bash
git clone <repository-url>
cd number-classification-api
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations
```bash
python manage.py migrate
```

### Start the Server
```bash
python manage.py runserver
```

### Testing Locally
Access the API via:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

## Deployment
The API is deployed on **Railway**. To deploy:
1. Push your code to GitHub.
2. Link your GitHub repository to Railway.
3. Configure environment settings.
4. Deploy and obtain a public endpoint.

## Version Control
- The project is hosted on a **public GitHub repository**.
- Includes a well-structured README.
- Uses Git for version control.

## Testing and Validation
Ensure the API meets all specifications before submission:
- ✅ Hosted on a publicly accessible platform
- ✅ Handles CORS
- ✅ Returns JSON responses
- ✅ Accepts valid integers only
- ✅ Implements proper error handling
- ✅ Thoroughly tested

## Submission Checklist
- [ ] Hosted API on a platform
- [ ] Double-checked all requirements
- [ ] Thoroughly tested the API
- [ ] Submitted via the designated form

## License
This project is open-source and available under the MIT License.

---

For any questions or contributions, feel free to open an issue or create a pull request on GitHub!

