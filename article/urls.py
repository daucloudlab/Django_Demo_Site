from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^1/$', basic_one, name="basic_one"),
    url(r'^2/$', template_two, name = "template_two"),
    url(r'^3/$', template_three, name = "template_three"),
    url(r'^$', articles, name = "all"),
    url(r'^get/(?P<article_id>\d+)/$',article, name = "detail"),
    url(r'^addlike/(?P<article_id>\d+)/$',addlike, name = 'addlike' ),
    url(r'^addcomment/(?P<article_id>\d+)/$', addcomment, name = 'addcomment')
]
