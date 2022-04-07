# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import add_user
from django.views.generic import TemplateView
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    re_path('add_user', add_user, name="add_user"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
