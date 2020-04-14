#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.hives, name='hives'),
    url(r'^add/$', views.add_hive, name='add_hive'),
    url(r'^zones/$', views.zone, name='zones'),
    url(r'^zones/edit/(?P<zone_id>[0-9]+)/$', views.edit_zone, name='edit_zone'),
    url(r'^zones/delete/(?P<zone_id>[0-9]+)/$', views.delete_zone, name='delete_zone'),
    url(r'^edit_hive/(?P<hive_id>[0-9]+)/$', views.edit_hive, name='edit_hive'),
    url(r'^delete_hive/(?P<hive_id>[0-9]+)/$', views.delete_hive, name='delete_hive'),
    url(r'^(?P<hive_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<hive_id>[0-9]+)/delete_history/(?P<history_id>[0-9]+)/$', views.delete_history, name='delete_history'),
]
