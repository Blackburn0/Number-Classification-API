import requests

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def get_fun_fact(n):
    response = requests.get(f'http://numbersapi.com/{n}/math')
    return response.text if response.status_code == 200 else 'No fact available.'
