from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('UNDER CONSTRUCTION! COMING SOON!')

def question_list(request):
   try:
        page = int(request.GET.get("page"))
   except ValueError:
        page = 1
   except TypeError:
        page = 1
   questions = Question.objects.all().order_by('-id')
   paginator = Paginator(questions, 10)
   page = paginator.page(page)
   return render(request, 'qlist.html',
                  {'title': 'Latest questions',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page, })
