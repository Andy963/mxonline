#!/usr/bin/env python
#coding:utf-8
#Created by Andy @ 2018/1/23


from django import forms
from operation.models import UserAsk
import re

# modelform的使用
class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]

    def clean_mobile(self):
        """
        验证手机号是否合法
        """
        mobile = self.cleaned_data["mobile"]
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")

