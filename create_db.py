# -*- coding: utf-8 -*-
import sqlite3
import time

connection = sqlite3.connect('vk.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE users (uid INTEGER PRIMARY KEY, first_name char(255) NOT NULL, last_name char(255) NOT NULL)")
cursor.execute("INSERT INTO users (uid, first_name, last_name) VALUES (213088,'Антон','Попов')")
cursor.execute("INSERT INTO users (uid, first_name, last_name) VALUES (599358,'Елена','Горшенина')")

cursor.execute("CREATE TABLE u213088 (time INTEGER PRIMARY KEY, status bool NOT NULL)")
cursor.execute("CREATE TABLE u599358 (time INTEGER PRIMARY KEY, status bool NOT NULL)")

cursor.execute("INSERT INTO u599358 (time, status) VALUES (" + str(int(time.time())) + ", 1)")

connection.commit()
connection.close()