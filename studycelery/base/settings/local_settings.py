from base.settings.base import *

DEBUG = True


__default_setting = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] [pid: %(process)d] [threadid: %(thread)d] [module: %(name)s] [%(pathname)s] [func: %(funcName)s] [line: %(lineno)d] [%(message)s]'
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}

for apps in INSTALLED_APPS:
    if apps.find('django') == -1:
        __default_setting['loggers'][apps] = {
            'handlers': ['console'],
            'level': 'ERROR'
        }

LOGGING = __default_setting


# DSM_HOST = '172.16.123.89'
# DSM_PORT = '5432'
# DSM_DBNAME = 'saoplatform_db'
# DSM_SCHEMA = 'saoplatform_schema'
# DSM_USER = 'service_app'
# DSM_PASSWORD = 'DBP!app123$'

