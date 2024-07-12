import os

from dotenv import load_dotenv
load_dotenv()

SENTRY_DSN = os.getenv('SENTRY_DSN')
DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUGSTATE = os.getenv('DEBUG')
