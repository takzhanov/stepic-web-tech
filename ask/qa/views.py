import datetime

from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from qa.models import Question, Answer, QuestionManager


def test(request, *args, **kwargs):
    return HttpResponse('test')


def new(request, *args, **kwargs):
    questions = QuestionManager.new(Question.objects)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)  # Page
    return render_to_response('questions.html', locals())


def popular(request, *args, **kwargs):
    questions = QuestionManager.popular(Question.objects)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)  # Page
    return render_to_response('questions.html', locals())


def question(request, id):
    try:
        q = Question.objects.get(id=id)
        answers = Answer.objects.filter(question=q)
    except Question.DoesNotExist:
        raise Http404
    return render_to_response('question.html', locals())


def time(request, *args, **kwargs):
    html = '<html><body>Time is %s</body></html>' % datetime.datetime.now()
    return HttpResponse(html)
