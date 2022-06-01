"""Platzigram views."""

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    # Convertimos el string devuelto por request.GET['numbers'] a una lista de números literales mediante
    numbers_literals = request.GET['numbers'].split(',')
    # Convertimos a números enteros los números literales mediante
    # list comprehension
    numbers = [int(i) for i in numbers_literals]
    sorted_ints = sorted(numbers)
    # La siguiente línea establece un debugger en tiempo de ejecución
    # import pdb; pdb.set_trace()
    # Construyamos un dict para luego transformarlo a un json
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    # Traduciendo el dict a un json y adaptando la respuesta a un json también
    # return HttpResponse(
    #     json.dumps(data, indent=4),
    #     content_type='application/json'
    # )
    # Otra opción para la respuesta JSON
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})

