#!/usr/bin/env python
#coding:utf-8
#Created by Andy @ 2017/10/21


from .models import Course, Lesson, Video, CourseResource
import xadmin

class CourseAdmin(object):
    list_display = ['name','desc', 'detail', 'degree','learn_time', 'students', 'fav_nums', 'click_num', 'add_time']
    search_fields= ['name','desc', 'detail', 'degree', 'students', 'fav_nums', 'click_num', 'add_time']
    list_filter= ['name','desc', 'detail', 'degree','learn_time', 'students', 'fav_nums', 'click_num', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields= ['course', 'name']
    list_filter= ['course__name', 'name', 'add_time']
    # 注意，Course是Lesson的一个外键，所以这里用course__name才能在后台显示出来


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)