from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question

#--------------------------------------------------------------------
def test(request, *args, **kwargs):
    return HttpResponse('UNDER CONSTRUCTION! COMING SOON!')


#--------------------------------------------------------------------
def paginate(request, qs):
    try:
         limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator
 

#---------------------------------------------------------------
def question_list(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1 
    # qs = Question.objects.all()
    # qs = qs.order_by('-id')
    # page, paginator = paginate(request, qs)
    # paginator.baseurl = reverse('question_list') + '?page='
    # return render(request, 'list.html', {
    #     'questions': page.object_list,
    #     'page': page,
    #     'paginator': paginator,
    # }) 
    return HttpResponse('Question list page '+str(page))
