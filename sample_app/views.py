# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from django import template

# Create your views here.

def pages(request):

    context ={
        "variable":"Simple Variable Injection",
        "bool_var":True,
        "list":[1, 2, 3, 4, 5]
    }

    requested_html = request.path.split('/')[-1]
    
    if not requested_html or requested_html == '':
        requested_html = 'index.html'

    try:

        html_file = loader.get_template( requested_html )
        return HttpResponse(html_file.render(context, request))    

    except template.TemplateDoesNotExist:

        return HttpResponse("template not found = " + requested_html, status=404)

    except:

        return HttpResponse("Error 500" , status=500)