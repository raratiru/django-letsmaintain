#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : letsmaintain/middleware.py
#
#       Creation Date : Wed 24 Jun 2020 07:20:58 PM EEST (19:20)
#
#       Last Modified : Wed 24 Jun 2020 08:26:26 PM EEST (20:26)
#
# ==============================================================================

from datetime import datetime, timedelta
from django.contrib import messages
from django.core.cache import cache
from django.utils import timezone
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = MaintenanceMessage(request).check_for_maintenance()
        return self.get_response(request)


class MaintenanceMessage:
    def __init__(self, request):
        self.request = request
        self.now = timezone.now()
        self.alert_time = datetime.fromisoformat(
            cache.get("maintenance_alert", "2020-06-10T00:00+00:00")
        )

    def check_for_maintenance(self):
        if self.now < self.alert_time:
            if (self.alert_time - self.now).seconds > 60:
                message_part_1 = gettext_lazy("Maintenance is scheduled for")
                message_part_2 = gettext_lazy("seconds remaining.")
                message = format_lazy(
                    "{part_1} {time}, {seconds} {part_2}",
                    part_1=message_part_1,
                    time=self.alert_time.strftime("%c %Z"),
                    seconds=(
                        self.alert_time - self.now - timedelta(seconds=60)
                    ).seconds,
                    part_2=message_part_2,
                )
                messages.warning(self.request, message)
            else:
                messages.error(
                    self.request, gettext_lazy("Maintenance is already in progress.")
                )
        return self.request
