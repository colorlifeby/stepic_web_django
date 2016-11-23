from django.conf.urls import url
from qa.views import test, question_list, popular, question_detail, question_ask, signup, login_view, logout_view

urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<ID>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^login/', login_view, name='login_view'),
    url(r'^logout/', logout_view, name='logout_view'),
    url(r'^signup/', signup, name='signup'),
    url(r'^new/', test, name='new'),
] 
