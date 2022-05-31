"""Platzigram views."""

# Django
from django.http import HttpResponse


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Hello, world!')
