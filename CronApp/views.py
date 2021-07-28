from django.shortcuts import render

# Create your views here.

import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse

def home(request):

    return HttpResponse('Django')
