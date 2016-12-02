from django import forms
from qa import models


class AskForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['title', 'text', 'author']
        #
        # def clean(self):
        #     return 1
        #
        # def save(self):
        #     return 1


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['text', 'author']

        # def clean(self):
        #     return 1
        #
        # def save(self):
        #     return 1