from rest_framework.decorators import api_view
from rest_framework.response import Response
from library.common import get_request_data
import pika


@api_view(['POST'])
def pika_test(request):
    print('hello pika task !!')

    # task 실행 소스
    params = get_request_data(request)
    params['body'] = "pika를 통해 큐에 적재하고자 하는 메세지"

    # RabbitMQ 에 데이터 추가하는 로직
    credentials = pika.PlainCredentials('guest', 'guest')
    queue_param = pika.ConnectionParameters(host='127.0.0.1',
                                            port=5672,
                                            virtual_host='studycelery',
                                            credentials=credentials,
                                            socket_timeout=5.0)
    connection = pika.BlockingConnection(queue_param)
    channel = connection.channel()
    channel.queue_declare(queue="myqueue", durable=True)
    ret = channel.basic_publish(exchange="", routing_key="myqueue", body=params['body'])
    connection.close()
    if ret:
        result = {"resultCode": 200, "resultData": [], "resultMsg": "success"}
    else:
        result = {"resultCode": 500, "resultData": [], "resultMsg": "error- rabbitMQ 데이터 추가 실패"}
    return Response(data=result)
