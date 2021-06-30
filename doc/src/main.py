#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author:- Femal Odedra
import cgi

from lib.service import URL_Detector
import logging
import json
import flask
import cgitb
cgitb.enable()


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

CGI = True
BadURL = True

cgitb.enable()

CGI = input("Enter proper url without space:")
print(CGI)
if CGI:
    URL = CGI
else:
    URL = "cx81.com"


Url_Info = URL_Detector(URL)

try:
    BadURL = Url_Info.URL_Search()
    logger.warning(BadURL)
except:
    print("URL Search error")
    raise

res = {}
if BadURL:
    logger.warning("The Url is Malicious")
    res[URL] = "Malicious"
else:
    res[URL] = "Good"
    logger.warning("The URL is Good")
print(json.dumps(res))
