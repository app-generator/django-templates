# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from sample_app import views

urlpatterns = [

    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
    re_path(r'', views.pages, name='pages'),

]
