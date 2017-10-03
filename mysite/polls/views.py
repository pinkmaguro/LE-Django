from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    current_time = datetime.datetime.now()
    context = {current_time : current_time}
    
    return HttpResponse('Hello Django.')
    # return render(request, 'polls/index.html')
