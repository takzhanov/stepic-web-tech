from django import forms
from qa import models
from django.contrib.auth.models import User


class AskForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['title', 'text', 'author']

    def clean(self):
        return self.cleaned_data

        # def save(self):
        #     return 1

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['text', 'question', 'author']

    def clean(self):
        return self.cleaned_data
        # def save(self):
        #     return 1

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        # User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        fields = ['username', 'email', 'password']

    def clean(self):
        return self.cleaned_data

        # def save(self):
        #     return 1

    # def __init__(self, *args, **kwargs):
    #     super(AskForm, self).__init__(*args, **kwargs)
    #     self.fields['author'].required = False



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        return self.cleaned_data