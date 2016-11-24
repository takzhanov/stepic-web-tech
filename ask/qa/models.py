from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Question(Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, on_delete=models.SET_NULL)


class Answer(Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)


class QuestionManager(models.Manager):
    def new(self):
        Question()

    def popular(self):
        []
