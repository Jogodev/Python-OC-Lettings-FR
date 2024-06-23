import os

from dotenv import load_dotenv

DJANGO_SECRET_KEY = os.getenv('SECRET_KEY')
SENTRY_DSN = os.getenv('SENTRY_DSN')
DEBUGSTATE = os.getenv('DEBUG')
