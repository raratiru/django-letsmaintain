[![Build Status](https://github.com/raratiru/django-letsmaintain/actions/workflows/python-package.yml/badge.svg)](https://github.com/raratiru/django-letsmaintain/actions)
[![Updates](https://pyup.io/repos/github/raratiru/django-letsmaintain/shield.svg)](https://pyup.io/repos/github/raratiru/django-letsmaintain/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Python Versions](https://img.shields.io/badge/Python-3.10|%203.11|%203.12|%203.13-%236600cc)](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)
[![Django Versions](https://img.shields.io/badge/Django-5.0%20|%205.1%20|%205.2-brown.svg)](https://www.djangoproject.com/download/)

# django-letsmaintain
Django middleware that provides a maintenance countdown warning message.


This middleware searches the cache for the key `maintenance_alert`. Its contents are expected to be a string representing an aware datetime in isoformat:

```python
from datetime import datetime, timezone

the_time = datetime.now(timezone.utc).isoformat(timespec='minutes')
print(the_time)
```
Example result: `'2020-06-24T12:00+00:00'`

* The middleware will raise a warning in all pages with a seconds countdown.

* The last 60 seconds, the warning message will become an error message.

A bash script can invoke the relevant cache key:

```bash
#!/bin/bash

FIVE_MINUTES_LATER=$(date --date "$(date +%Y-%m-%dT%H:%M:%S%:z) +5 min" --iso-8601=minutes)
echo "from django.core.cache import cache; cache.set(\"maintenance_alert\", \"$FIVE_MINUTES_LATER\")" \
  | ./manage.py shell
sleep 5m
# Redirect to maintenance.html
# nginx example: https://lincolnloop.com/blog/pro-tip-redirecting-custom-nginx-maintenance-page/
# <perform maintenance>
# Cancel redirect
```

## Required Settings
The required settings for the middleware to operate are:

* `CACHES`
* `TIME_ZONE`
* `USE_TZ = True`
* "letsmaintain" in `INSTALLED_APPS`
* "letsmaintain.middleware.MaintenanceMiddleware" in `MIDDLEWARE` after "MessageMiddleware"

## Tests

To run the tests:

* Install tox
* Define: `TOX_DB_NAME`, `TOX_DB_USER`, `TOX_DB_PASSWD`
