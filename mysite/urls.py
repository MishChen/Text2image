#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'excute.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cut/$', 'excute.views.jiebaCut', name='jiebaCut'),
    url(r'^cut1/$', 'excute.views.jiebaCut1', name='jiebaCut'),
    url(r'^profile/$', 'excute.views.profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)