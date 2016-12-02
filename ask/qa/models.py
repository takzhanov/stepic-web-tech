from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, Count
from django.utils import timezone


class QuestionManager(models.Manager):
    def new(self):
        return (self.order_by('-added_at'))

    def popular(self):
        return (self.annotate(num_likes=Count('likes')).order_by('num_likes'))


class Question(Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now, null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author')
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

    def get_url(self):
        return '/question/' + str(self.id) + '/'

    def __str__(self):
        return '(id=' + str(self.id) + ', added_at=' + str(self.added_at)


class Answer(Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)
