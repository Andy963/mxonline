#!/usr/bin/env python
#coding:utf-8
#Created by Andy @ 2018/1/27


from django.conf.urls import url, include
from .views import CourseListView
urlpatterns = [
    url(r'^list/$',CourseListView.as_view(), name='course_list'),

]


