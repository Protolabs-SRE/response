from .base import *

SITE_URL = "http://localhost:8000"

if "TUNNEL_HOSTNAME" in os.environ:
    SITE_URL =  os.environ.get("TUNNEL_HOSTNAME")

if os.environ.get("POSTGRES"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': 'db',
            'PORT': '5432',
            'USER': 'postgres',
            'NAME': 'postgres',
        }
    }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': " {levelname:5s} - {module:10.15s} - {message}",
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}


SLACK_TOKEN = get_env_var("SLACK_TOKEN", True)
SLACK_SIGNING_SECRET = get_env_var("SLACK_SIGNING_SECRET", True)
INCIDENT_CHANNEL_NAME = get_env_var("INCIDENT_CHANNEL_NAME", True)
INCIDENT_BOT_NAME = get_env_var("INCIDENT_BOT_NAME", True)
STATUS_PAGE_RUNBOOK_URL = get_env_var("STATUS_PAGE_RUNBOOK", True)
RUNBOOKS_URL = get_env_var("RUNBOOKS_URL", True)

try:
    INCIDENT_BOT_ID = get_user_id(INCIDENT_BOT_NAME, SLACK_TOKEN)
except:
    INCIDENT_BOT_ID = None

try:
    INCIDENT_CHANNEL_ID = get_channel_id(INCIDENT_CHANNEL_NAME, SLACK_TOKEN)
except:
    INCIDENT_CHANNEL_ID = None
