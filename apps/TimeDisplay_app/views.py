from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import *
from time import gmtime, strftime
from datetime import datetime, date, time

import datetime

def index(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, "TimeDisplay_app/index.html", context)
