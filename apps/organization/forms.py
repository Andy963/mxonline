#!/usr/bin/env python
#coding:utf-8
#Created by Andy @ 2018/1/23


from django import forms
from operation.models import UserAsk


class UserAskForm(forms.Form):
    name = forms.CharField(required=True, min_length=2, max_length=20)
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    course_name = forms.CharField(required=True, min_length=5, max_length=5)

# modelform的使用
class AnotherUserForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']