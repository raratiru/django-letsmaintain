#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : test_setup/settings.py
#
#       Creation Date : Wed 24 Jun 2020 07:23:23 PM EEST (19:23)
#
#       Last Modified : Wed 24 Jun 2020 08:27:16 PM EEST (20:27)
#
# ==============================================================================

import os
from collections import namedtuple

Settings = namedtuple("Settings", ["username", "password"])

db = {
    "django.db.backends.postgresql": Settings(
        username=os.environ.get("POSTGRES_USER", os.environ.get("TOX_DB_USER")),
        password=os.environ.get("POSTGRES_PASSWD", os.environ.get("TOX_DB_PASSWD")),
    ),
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    "default": {
        "ENGINE": os.environ["TOX_DB_ENGINE"],
        "NAME": os.environ["TOX_DB_NAME"],
        "USER": db[os.environ["TOX_DB_ENGINE"]].username,
        "PASSWORD": db[os.environ["TOX_DB_ENGINE"]].password,
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "letsmaintain",
]

LANGUAGE_CODE = "en"

LANGUAGES = (("en", "English"),)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "letsmaintain.middleware.MaintenanceMiddleware",
]

ROOT_URLCONF = "test_setup.urls"

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

SECRET_KEY = "ssdflkjhn430934ljkndf09324lkjnrfdg-0fghngnjmjk0i934jn"

TIME_ZONE = "Europe/Athens"

USE_TZ = True
