from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm

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
                   'page': page, })

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
                   'page': page, })


def question_detail(request, ID,):
    questionObj = get_object_or_404(Question, pk=ID)
    answers = Answer.objects.filter(question = questionObj)

    if request.method == "POST":
       form = AnswerForm(request.POST)
       if form.is_valid():
          form._user = 1
          answer = form.save()
          return HttpResponseRedirect(questionObj.get_url())
    else:
       form = AnswerForm(initial={'question': questionObj.id})

    return render(request, 'question.html', {'question': questionObj,
                                             'answers':answers,
                                             'form': form, }) 
