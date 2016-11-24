from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, Count
from django.utils import timezone


class Question(Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author')
    likes = models.ManyToManyField(User)


class Answer(Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)


class QuestionManager(models.Manager):
    def new(self):
        return (self.order_by('-added_at'))

    def popular(self):
        return (self.annotate(num_likes=Count('likes')).order_by('num_likes'))
