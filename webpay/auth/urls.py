from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',  # noqa
    url(r'^verify$', views.verify, name='auth.verify'),
    url(r'^reverify$', views.reverify, name='auth.reverify'),
)
