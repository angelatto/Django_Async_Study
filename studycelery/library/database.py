from django.conf import settings
import psycopg2


class DatabaseNotExistsError(Exception):
    def __str__(self):
        return "데이터베이스에 연결할 수 없습니다. 존재하는 회사에 연결을 시도했는지 확인 해 주세요."


class get_connection(object):
    """
    DB Connection 공통 함수
    """
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(user='homecj',
                                         host='localhost',
                                         dbname='postgres',
                                         password='zzzzz',
                                         port='5432'
                                         )

            import psycopg2.extensions as _ext
            self.conn.set_isolation_level(_ext.ISOLATION_LEVEL_AUTOCOMMIT)
        except Exception as e:
            raise e

    def __enter__(self):
        self.cursor = self.conn.cursor()

        if self.cursor:
            return self.cursor
        else:
            raise DatabaseNotExistsError

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
            self.conn.close()

