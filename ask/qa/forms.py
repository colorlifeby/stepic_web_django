from django.shortcuts import get_object_or_404
from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
#    question = forms.IntegerField()

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip()=='':
           raise forms.ValidationError(u'Answer is empty', code = 12)
        return text

    def save(self):
        # self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        self.cleaned_data['author_id'] = 1
        answ = Answer(**self.cleaned_data)
        answ.save()
        return answ

