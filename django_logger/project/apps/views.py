import json

from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
import logging

logger = logging.getLogger('django')


def login_view(request):
    logger.info("Das ist info")
    logger.warning("Das ist warning")
    logger.error("Das ist error")
    logger.critical("Das ist critical error")

    return HttpResponse("<h1  > Test </h1>")
