import os
from settings import BASE_DIR

def rel(*x):
    return os.path.join(BASE_DIR, *x)

LANGUAGE_CODE = 'ru'

TEMPLATE_DIRS = (
    rel('templates'),
)

STATICFILES_DIRS = (
    rel('static'),
    rel('bootstrap'),
    rel('grapelli'),
    rel('ext-3'),
)