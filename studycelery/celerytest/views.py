from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from library.common import get_request_data
from .task import *


@api_view(['POST'])
def celery_test(request):
    params = get_request_data(request)
    print('hello celery task !!')

    # task 실행 소스
    for id in range(1, 6):
        celery_worker.delay(params, id)

    result = {
        'result_code': status.HTTP_200_OK,
        'result_msg': 'rabbitmq task 적재',
        'result_data': '',
    }
    return Response(data=result)