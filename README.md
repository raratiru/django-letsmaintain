# django-letsmaintain
Django middleware for maintenance countdown warning message

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
echo "from django.core.cache import cache; cache.set(\"maintenance_alert\", \"$FIVE_MINUTES_LATER\")" | ./manage.py shell
sleep 5m
# Redirect to maintenance.html 
# nginx example: https://lincolnloop.com/blog/pro-tip-redirecting-custom-nginx-maintenance-page/
# <perform maintenance>
# Cancel redirect
```
