from django.conf.urls import url
from qa.views import test, question_list

urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<ID>\d+)/', test, name='question_detail'),
    url(r'^popular/', test, name='popular'),
    url(r'^ask/', test, name='question_ask'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^new/', test, name='new'),
] 
