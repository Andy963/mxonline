#!/usr/bin/env python
# coding:utf-8
# Created by Andy @ 2018/2/7


from django.conf.urls import url, include
from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView

urlpatterns = [
    # 课程列表页
    url(r'^info/$', UserinfoView.as_view(), name='user_info'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 发送邮箱验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 发送邮箱验证码
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    # 我的消息
    # url(r'^my_message/$', MyMessageView.as_view(), name='my_message'),
]
