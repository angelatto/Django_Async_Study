def get_request_data(request):
    _data = None

    if request.method == 'GET':
        _data = request.query_params.copy()
    else:
        _data = request.data.copy()

    return _data