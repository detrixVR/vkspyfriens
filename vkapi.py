#!/usr/bin/env python2.7 -tt
# -*- coding: utf-8 -*-
"""

  For this we gonna use getProfiles API method. For one
  request we can get info about up to 990 users. It makes
  this perfect for our task.

  Update time is about 3 mins.

  get_status method returns dictionary in format:
  {userid: 1 for Online,  0 for Offline}


"""

__author__  = "Ademaro"
__url__     = "https://github.com/Ademaro/vk"

if __name__ == "__main__": quit()

import time
import sqlite3
import json
import urllib2
import logging

VK_GETPROFILES_BASE = 'https://api.vkontakte.ru/method/getProfiles?uids='

class Collector:

  def get_status(self, list_for_check):
    """
      getProfiles, up to 990 users.

    """
    d = {} # dictionary for return
    if len(list_for_check) > 990:
      return "Error, too much to check"
    elif len(list_for_check) == 0:
      logging.warning("[Collector] Passed empty list to check")
      return "Error, nothing to check"

    vkids = ",".join((str(i) for i in list_for_check))
    logging.info("[Collector] Making getProfiles API request...")
    request = VK_GETPROFILES_BASE+vkids+"&fields=online"

    try:
      jsondata = json.loads(urllib2.urlopen(request, None, 25).read())
    except (URLError, HTTPError):
      logging.error("[Collector] Some error happaned during getProfiles API request")
    # if jsondata['error']: logging.error("Cannot get correct API response.")

    connection = sqlite3.connect('vk.db')
    cursor = connection.cursor()

    for i in jsondata['response']:
      d[i['uid']] = i['online']
      cursor.execute("SELECT * from u" + str(i['uid']) + " order by time desc limit 1")
      last_status = cursor.fetchone()
      #print(i['uid'],last_status[1],i['online'])
      if last_status[1] != i['online']:
          cursor.execute("INSERT INTO u" + str(i['uid']) + "(time, status) VALUES (" + str(int(time.time())) + "," + str(i['online']) + ")")
          logging.info("[Collector] Add record for : " + str(i['uid']) + " ")
    logging.info("[Collector] Request has been parsed, records: "+str(len(d))+" ")
    connection.commit()
    connection.close()
    return d

  def last_status(self, list_for_check):
      """
        display last status
      """
      d = {}
      if len(list_for_check) > 990:
        return "Error, too much to check"
      elif len(list_for_check) == 0:
        logging.warning("[Collector] Passed empty list to check")
        return "Error, nothing to check"

