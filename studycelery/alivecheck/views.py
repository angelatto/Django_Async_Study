from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def alive_check(request):
    if request.method == 'GET':
        return Response(data='Hello alivecheck')
