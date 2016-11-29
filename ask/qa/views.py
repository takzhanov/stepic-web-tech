from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('test')


def new(request, *args, **kwargs):
    return HttpResponse('new')


def popular(request, *args, **kwargs):
    return HttpResponse('popular')


def question(request, *args, **kwargs):
    return HttpResponse('question')
