#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015
# Gmail:liuzheng712
#
__author__ = 'liuzheng'

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    user = request.GET.get('u','').strip()
    container = request.GET.get('c','').strip()
    if (user == '') and (container == ''):
        return HttpResponse('index.html')
    else:
        return HttpResponse('Hello User:'+user+',your are in container:'+container)

