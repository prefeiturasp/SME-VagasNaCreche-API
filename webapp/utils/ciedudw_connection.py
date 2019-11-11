import os

import psycopg2


class CIEDUDWConnection:

    def __init__(self):
        self.host = os.environ.get('CIEDUDW_HOST')
        self.user = os.environ.get('CIEDUDW_USER')
        self.passd = os.environ.get('CIEDUDW_PASS')
        self.db = os.environ.get('CIEDUDW_DB')

    def querie(self, query):
        try:
            with psycopg2.connect(host=self.host, user=self.user, password=self.passd,
                                  dbname=self.db) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                response = {'results':
                                [dict(zip([column[0] for column in cursor.description], row))
                                 for row in cursor.fetchall()]}
        except psycopg2.Error as e:
            response = f'ERROR',e

        return response
