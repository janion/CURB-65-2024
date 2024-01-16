from sqlite3 import connect, Error
from contextlib import closing

_create_table = """CREATE TABLE IF NOT EXISTS curb_score (
                                pid text NOT NULL,
                                dob text NOT NULL,
                                doc text NOT NULL,
                                confusion integer NOT NULL,
                                urea real NOT NULL,
                                resp_rate real NOT NULL,
                                bps real NOT NULL,
                                bpd real NOT NULL,
                                score integer NOT NULL
                            );"""


class Database(object):

    def __init__(self):
        with closing(connect('curb.db')) as connection:
            # create tables
            if connection is not None:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(_create_table)

    def add_score(self, pid, dob, doc, confusion, urea, resp_rate, bps, bpd, score):
        with closing(connect('curb.db')) as connection:
            with closing(connection.cursor()) as cursor:
                sql = f'INSERT INTO curb_score VALUES ("{pid}", "{dob}", "{doc}", "{confusion}", "{urea}", "{resp_rate}", "{bps}", "{bpd}", "{score}")'
                cursor.execute(sql)
