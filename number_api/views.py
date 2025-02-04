
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import is_prime, is_perfect, is_armstrong, get_fun_fact

@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number')
    try:
        number = int(number)
    except (TypeError, ValueError):
        return Response({'number': "alphabet", 'error': True}, status=400)
    
    properties = []
    if is_armstrong(number):
        properties.append('armstrong')
    properties.append('odd' if number % 2 else 'even')
        
    return Response({
        'number': number,
        'is_prime': is_prime(number),
        'is_perfect': is_perfect(number),
        'properties': properties,
        'digit_sum': sum(int(d) for d in str(number)),
        'fun_fact': get_fun_fact(number)
    })
