from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Question, Choice

def index(request):
    current_time = datetime.datetime.now()
    
    #return HttpResponse('Hello Django.')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,
                'name':'Ryan Kang',
                'today': current_time}  # strftime('%Y-%m-%d')
    return render(request, 'polls/index.html', context)

