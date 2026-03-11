import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_noticeboard.settings")

application = get_wsgi_application()
