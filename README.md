[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/raratiru/django-letmaintain.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/raratiru/django-letsmaintain/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/61b3e157f170421ca3388f83567a873a)](https://www.codacy.com/app/raratiru/django-letsmaintain?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=raratiru/django-letsmaintain&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.com/raratiru/django-letsmaintain.svg?branch=master)](https://travis-ci.com/raratiru/django-letsmaintain)
[![Coverage Status](https://coveralls.io/repos/github/raratiru/django-letsmaintain/badge.svg?branch=travis)](https://coveralls.io/github/raratiru/django-letsmaintain?branch=travis)
[![Updates](https://pyup.io/repos/github/raratiru/django-letmaintain/shield.svg)](https://pyup.io/repos/github/raratiru/django-letsmaintain/)
[![Known Vulnerabilities](https://snyk.io/test/github/raratiru/django-letsmaintain/badge.svg?targetFile=test_setup%2Frequirements.txt)](https://snyk.io/test/github/raratiru/django-letsmaintain?targetFile=test_setup%2Frequirements.txt)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Python Versions](https://img.shields.io/badge/Python-3.7%20|%203.8-%236600cc)](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)
[![Django Versions](https://img.shields.io/badge/Django-2.2%20|%203.0-brown.svg)](https://www.djangoproject.com/download/)

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
