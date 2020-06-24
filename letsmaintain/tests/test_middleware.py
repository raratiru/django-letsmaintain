#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : letsmaintain/tests/test_middleware.py
#
#       Creation Date : Wed 24 Jun 2020 07:21:36 PM EEST (19:21)
#
#       Last Modified : Wed 24 Jun 2020 07:36:49 PM EEST (19:36)
#
# ==============================================================================

from datetime import timedelta, datetime, timezone
from django.core.cache import cache
from django.urls import reverse


def test_middleware_not_set(client):
    cache.delete("maintenance_alert")
    cache_not_set = client.get(reverse("admin:login")).rendered_content
    assert "Maintenance is scheduled for" not in cache_not_set


def test_middleware_set_over_60(client):
    cache.set(
        "maintenance_alert",
        (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat(
            timespec="minutes"
        ),
    )
    cache_set = client.get(reverse("admin:login")).rendered_content
    assert "Maintenance is scheduled for" in cache_set
    assert "in progress" not in cache_set


def test_middleware_set_under_60(client):
    cache.set(
        "maintenance_alert",
        (datetime.now(timezone.utc) + timedelta(seconds=55)).isoformat(
            timespec="minutes"
        ),
    )
    cache_set = client.get(reverse("admin:login")).rendered_content
    assert "in progress" in cache_set
    assert "Maintenance is scheduled for" not in cache_set
