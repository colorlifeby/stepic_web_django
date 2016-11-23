# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    
    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

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

    def clean(self):
        return self.cleaned_data

    def save(self):
        answ = Answer(**self.cleaned_data)
        answ.author_id = self._user.id
        answ.save()
        return answ


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Не задано имя пользователя', code = 12)
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('Такой пользователь уже существует', code = 12)
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Не указан адрес электронной почты', code = 12)
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль', code = 12)
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class LoginForm(forms.Form):
    username = forms.CharField( max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Не задано имя пользователя')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль')
        return password

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = authenticate(**self.cleaned_data)
        return user
