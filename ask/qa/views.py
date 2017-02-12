import datetime

from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from qa import forms
from qa.models import Question, Answer, QuestionManager
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
            form.author = request.user
            if form.is_valid():
                new_answer = form.save(commit=False)
                # new_answer.question = q
                new_answer.save()
                url = q.get_url()
                return HttpResponseRedirect(url)
        else:
            form = forms.AnswerForm(initial={'question': q})
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', locals())


def new_question(request):
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        form.author = request.user
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


def signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            dbuser = User.objects.get(username=username)
            print(dbuser.password)
            print(password)
            print(dbuser.check_password(password))
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            print(authenticate(username='tt', password='tt'))
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {
                    'form': form,
                    'invalid': True
                })
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {
        'form': form
    })

