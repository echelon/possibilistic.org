from django.conf.urls.defaults import *

urlpatterns = patterns('possibilistic.mpages.views',
    (r'^/?$', 'index'),
    (r'^(?P<page_name>[\w\-\/]+)/$', 'view_page'),
)

