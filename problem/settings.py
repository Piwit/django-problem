from django.conf import settings

app_settings = getattr(settings, 'PROBLEM', {})

PAGES = app_settings['PAGES'] if 'PAGES' in app_settings else (('-', '-'),)
