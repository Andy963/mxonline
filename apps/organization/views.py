# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class OrgView(View):
    """
    课程机构列表
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('click_nums')[:3]
        #城市
        all_citys = CityDict.objects.all()
        city_id = request.GET.get('city', '')
        # 筛选城市
        if city_id :
            all_orgs = all_orgs.filter(city=int(city_id))

        # 筛选类别
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)


        sort= request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page =1
        p = Paginator(all_orgs, 5, request=request)
        people = p.page(page)
        orgs = p.page(page)
        return render(request, 'org-list.html',
                      {'all_orgs':orgs,
                       'all_citys':all_citys,
                       'org_num':org_nums,
                       'category': category,
                       'hot_orgs':hot_orgs,
                       'sort':sort
                       })
