import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    INSTALLED_APPS=('tests',)
)
django.setup()

test_runner = DiscoverRunner(verbosity=1)
if failures := test_runner.run_tests([]):
    sys.exit(failures)
