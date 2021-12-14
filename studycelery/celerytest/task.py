import json
from base.celery import app
import time
import random

# 여기서 app은 셀러리 인스턴스를 의미함 ! 임포트 주의
@app.task(name='msg_chaejeong')
def celery_worker(params, id=1):
    # 1~5초 사이의 랜덤한 Delay를 발생.
    json_params = json.dumps(params)
    time.sleep(random.randint(1, 10))

    print('hello celery worker~~!!')
    print(json_params)
    print('{}번째, 일을 끝냈다.'.format(id))

    # 여기서 리턴값이 레디스에 저장되는데, 키값은 임의로 들어가고 있음..
    return '{} <- finish work'.format(id)
