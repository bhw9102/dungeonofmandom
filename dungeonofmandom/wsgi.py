"""
WSGI config for dungeonofmandom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import newrelic.agent
from django.core.wsgi import get_wsgi_application
import platform

if platform.system() == 'linux':
    newrelic.agent.initialize('/var/lib/jenkins/workspace/dungeonofmandom/newrelic.inios.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dungeonofmandom.settings')

application = get_wsgi_application()

if platform.system() == 'linux':
    application = newrelic.agent.wsgi_application()(application)
