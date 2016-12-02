import datetime

from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from qa import forms
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
        if request.method == "POST":
            form = forms.AnswerForm(request.POST)
            if form.is_valid():
                new_answer = form.save(commit=False)
                # new_answer.question = q
                new_answer.save()
                url = q.get_url()
                return HttpResponseRedirect(url)
        else:
            form = forms.AnswerForm(request.POST)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', locals())


def new_question(request):
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.AskForm()
    return render(request, 'new_question.html', {
        'form': form
    })


def time(request, *args, **kwargs):
    html = '<html><body>Time is %s</body></html>' % datetime.datetime.now()
    return HttpResponse(html)
