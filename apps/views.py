# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request, "form/register.html")
# Create your views here.
