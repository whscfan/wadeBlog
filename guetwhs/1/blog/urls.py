#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author: whscfan
# Created At:  下午12:31
# Filename: urls
# Description:
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from views import *
urlpatterns = [
    url(r'^$',articleList.as_view(template_name='blog/index.html'),name="index"),
    url(r'^detail/(?P<pk>\w+)/$',articleDetail.as_view(),name="detail"),
    url(r'^edit/(?P<pk>\w+)/$',articleUpdate.as_view(),name="edit"),
    url(r'^delete/(?P<pk>\w+)/$',articleDelete.as_view(),name="delete"),
    url(r'^about/$',about.as_view(),name="about"),
    url(r'^create/$',articleCreate.as_view(template_name='blog/create.html'),name="create"),
    url(r'^user/(?P<option>\w+)/$',userCenter.as_view(),name="userCenter"),
    url(r'^category/$',categoryList.as_view(),name="category"),
    url(r'^accounts/login/$',TemplateView.as_view(template_name='blog/login.html'),name='login'),
    url(r'^category/(?P<pk>\w+)/$',categoryUpdate.as_view(),name='categoryUpdate'),
    url(r'^category_delete/(?P<pk>\w+)/$',categoryDelete.as_view(),name='categoryDelete'),
    url(r'^categoryCreate/$',categoryCreate.as_view(),name='categoryCreate'),
    url(r'^search/$',search.as_view(),name='search'),
    url(r'^comment/(?P<pk>\w+)/$',commentCreate.as_view(),name='comment'),
    url(r'^category/list/(?P<pk>\w+)/$',article_by_category.as_view(),name="listByCategory"),
    url(r'^tag/list/(?P<pk>\w+)/$',article_by_tag.as_view(),name="tag"),
    url(r'^about/modify/(?P<pk>\w+)/$',updateAbout.as_view(),name="updateAbout"),
    url(r'^link_create/$',linkCreate.as_view(),name="linkCreate"),
]