# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

# --------브로커 공통 url--------
INIT_BROKER_URL = "amqp://guest:guest@localhost:5672/"
# --------task result backend 설정--------
result_backend = "redis://localhost:6379"
# --------브로커 설정--------
# VM_DATAEXPORT = ["172.16.123.109","172.16.123.110","10.106.3.60"]

# if ip in VM_DATAEXPORT:
# -------- rabbitmq vhost --------
broker_url = INIT_BROKER_URL
# broker_url = INIT_BROKER_URL + "pudri"

accept_content = ['json']
result_serializer = 'json'

# 기본설정
enable_utc = True
timezone = 'Asia/Seoul'
task_serializer = 'json'

# Task 세팅
task_annotations = {'*': {'rate_limit': '10/s'}}
task_time_limit = 83400
task_soft_time_limit = 43200

# Result 세팅
result_expires = 43200
task_ignore_result = False

# Error 발생시 메일 전송(admins email)
CELERY_SEND_TASK_ERROR_EMAILS = True

# Name and email addresses of recipients
ADMINS = ('pudri', 'dlcowjd0322@douzone.com')

SERVER_EMAIL = 'dlcowjd0322@douzone.com'
EMAIL_PORT = 25

# 서비스 key
# SERVICE_CODE = 'smarta'
# SERVICE_KEY = '769802f060aa11e78e24f760d7907e9f'

# CELERY_IMPORTS = ('migration_app.tasks',)
# celery schedule
# CELERYBEAT_SCHEDULE = {
#     'migration_scheduler_job': {
#         'task': 'migration_scheduler',
#         'schedule': timedelta(seconds=10)
#     }
# }

