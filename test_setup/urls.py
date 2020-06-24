#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : test_setup/urls.py
#
#       Creation Date : Wed 24 Jun 2020 07:22:39 PM EEST (19:22)
#
#       Last Modified : Wed 24 Jun 2020 07:23:10 PM EEST (19:23)
#
# ==============================================================================

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
