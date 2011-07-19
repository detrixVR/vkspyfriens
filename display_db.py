# -*- coding: utf-8 -*-
__author__ = 'Ademaro'

import sqlite3
from datetime import datetime

connection = sqlite3.connect('vk.db')
cursor = connection.cursor()

print("\nFOR Anton:")
cursor.execute('select * from u213088')
for row in cursor:
  print datetime.fromtimestamp(row[0]), 'в сети' if row[1] else 'не в сети'

print("\nFOR Lena:")
cursor.execute('select * from u599358')
for row in cursor:
    print datetime.fromtimestamp(row[0]), 'в сети' if row[1] else 'не в сети'
