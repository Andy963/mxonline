# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural=verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    comment = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(choices=())
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'用户消息')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

