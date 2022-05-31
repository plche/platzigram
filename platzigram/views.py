"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    """Hi."""
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    # print(numbers)
    # return HttpResponse('Hi!')
    return HttpResponse(str(numbers))
