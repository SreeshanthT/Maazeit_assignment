from django.conf import settings

import sqlite3
import os

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

db_path = os.path.join(settings.BASE_DIR,"db.sqlite3")

sql_con = sqlite3.connect(db_path,check_same_thread=False)



