from django.conf.urls import patterns, include, url

urlpatterns = patterns('myproject.brdesigner.views',
   url(r'^$','gateway', name='static_home'),
   url(r'^(?P<path>.+?)/$','gateway', name='static_home'),
)
