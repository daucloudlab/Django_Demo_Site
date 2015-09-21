from django.conf.urls import include, url
from views import basic_one, template_two, template_three, articles, article

urlpatterns = [
    url(r'^1/$', basic_one, name="basic_one"),
    url(r'^2/$', template_two, name = "template_two"),
    url(r'^3/$', template_three, name = "template_three"),
    url(r'^$', articles, name = "all"),
    url(r'^get/(?P<article_id>\d+)/$',article, name = "detail")
]
