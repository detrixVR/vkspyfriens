#!/usr/bin/env python2.7 -tt
# -*- coding: utf-8 -*-

__author__ = 'Ademaro'
__url__     = "https://github.com/Myuzu/shy-spy"

from multiprocessing import Process
import os, sys
import sqlite3
import time
import logging

import vkapi as coll

APP_ID = 'vk'

def get_list_for_check():
  """ Getting list of user ID's for check """
  listik = list()

  connection = sqlite3.connect('vk.db')
  cursor = connection.cursor()
  cursor.execute("SELECT uid from users")

  for row in cursor:
      listik.append(row[0])
#    listik.append(1)
#    listik.append(7066621)
#    listik.append(4012634)
#    listik.append(9890838)
#    listik.append(27790460)
#    listik.append(35074591)
#    listik.append(13683433)
#    listik.append(77721563)

  return listik


def main():
  try:
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        filename='debug.log',
                        level=logging.DEBUG)
  except IOError:
    logging.warning('[VK Main] Log file not exists, creating...')
    try:
      open(r"debug.log", "w").write("Creating new log file...\n")
    except IOError:
      logging.error('[VK Main] Cannot create a log file, quiting...')
      quit()

  try:
    while True:
      list_for_check = get_list_for_check()
      vk = coll.Collector()
      vk.get_status(list_for_check)
      time.sleep(15)
  except (KeyboardInterrupt):
    logging.info('[VK Main] Stopped by user!\n')
    print "\n\nStopped by user"


if __name__ == "__main__":
  main()
