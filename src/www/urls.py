from django.conf.urls import patterns, include, url


urlpatterns = patterns('www.views',
    url(r'^$', 'index', name='home_view'),
    url(r'^(?P<slug_name>[-\w]+)/$', 'post', name='post_view'),
)