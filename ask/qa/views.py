# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse('UNDER CONSTRUCTION! COMING SOON!')


def question_list(request):
   try:
        page = int(request.GET.get("page"))
   except ValueError:
        page = 1
   except TypeError:
        page = 1
   questions = Question.objects.all().order_by('-added_at')
   paginator = Paginator(questions, 10)
   page = paginator.page(page)
   return render(request, 'qlist.html',
                  {'title': 'Latest questions',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })

def popular(request):
   try:
        page = int(request.GET.get("page"))
   except ValueError:
        page = 1
   except TypeError:
        page = 1
   questions = Question.objects.all().order_by('-rating')
   paginator = Paginator(questions, 10)
   page = paginator.page(page)
   return render(request, 'qlist.html',
                  {'title': 'Popular questions',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })


def question_detail(request, ID,):
    questionObj = get_object_or_404(Question, pk=ID)
    answers = Answer.objects.filter(question = questionObj)

    if request.method == "POST":
       form = AnswerForm(request.POST)
       if form.is_valid():
          form._user = request.user
          answer = form.save()
          return HttpResponseRedirect(questionObj.get_url())
    else:
       form = AnswerForm(initial={'question': questionObj.id})

    return render(request, 'question.html', {'question': questionObj,
                                             'answers':answers,
                                             'form': form,
                                             'user': request.user,
                                             'session': request.session, })


def question_ask(request):
    if request.method == "POST":
       form = AskForm(request.POST)
       if form.is_valid():
          form._user = request.user
          questionObj = form.save()
          return HttpResponseRedirect(questionObj.get_url())
    else:
       form = AskForm()
    return render(request, 'ask.html', {'form': form,
                                        'user': request.user,
                                        'session': request.session, })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
               login(request, user)
               return HttpResponseRedirect('/')
    form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session, })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
               logout(request)
               login(request, user)
               return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form': form,
                                          'user': request.user,
                                          'session': request.session, })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
