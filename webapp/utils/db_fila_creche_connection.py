import os

import psycopg2


class FilaDBConnection:

    def __init__(self):
        self.host = os.environ.get('FILADB_HOST')
        self.user = os.environ.get('FILADB_USER')
        self.passd = os.environ.get('FILADB_PASS')

    def querie(self, query):
        try:
            with psycopg2.connect(host=self.host, user=self.user, password=self.passd, dbname="postgres",
                                  port=5433) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                response = {'results':
                                [dict(zip([column[0] for column in cursor.description], row))
                                 for row in cursor.fetchall()]}
        except psycopg2.Error as e:
            response = f'ERROR'

        return response
