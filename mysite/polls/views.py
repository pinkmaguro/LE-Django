from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)