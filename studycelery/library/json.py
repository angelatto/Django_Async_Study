import json
from collections import OrderedDict


def name_to_json(cursor, empty=False, bsort=False, bUpper=False):
    """
    cursor.fetchall() 함수로 받아온 쿼리 결과를 json 형식으로 만들어 반환해주는 함수입니다.
    :param cursor: SQL 연결 변수
    :return: JSON 쿼리 결과 LIST
    """
    dic = {}
    row = []
    if cursor.rowcount > 0 :
        if bsort:
            row = [OrderedDict((cursor.description[i][0].upper() if bUpper == True else cursor.description[i][0], value)
                        for i, value in enumerate(row)) for row in cursor.fetchall()]
        else:
            row = [dict((cursor.description[i][0].upper() if bUpper == True else cursor.description[i][0], value)
                               for i, value in enumerate(row)) for row in cursor.fetchall()]
    else:
        if empty:
            for col in cursor.description:
                dic[col.name.upper() if bUpper == True else col.name] = None
            row.append(dic.copy())
    return row