from django.shortcuts import render
from django.http import HttpResponse
import time
from datetime import timedelta
from datetime import datetime
from datetime import date
import json
from time import gmtime, strftime
import os
from django.template import loader

def index(request):
    try:
        context = {}
        template = loader.get_template('config/index.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        print(e)
        raise e

